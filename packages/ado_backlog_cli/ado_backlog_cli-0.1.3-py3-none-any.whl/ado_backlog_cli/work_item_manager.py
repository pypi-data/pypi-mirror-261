"""
WorkItemManager class for querying and fetching Azure DevOps work items.

Provides methods to query work items using WiQL, fetch work item details in batches, 
and recursively fetch related work items. Uses thread pools and async tasks to fetch
work items concurrently.
"""
import logging
import os
import psutil
from functools import wraps
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.work_item_tracking.models import Wiql
from concurrent.futures import ThreadPoolExecutor, as_completed
from .work_item import WorkItem

logger = logging.getLogger(__name__)

"""Initializes a WorkItemManager instance.

Args:
    org_url: The URL of the Azure DevOps organization. 
    personal_access_token: Personal access token for authenticating to Azure DevOps.
    project_name: Name of the Azure DevOps project.

Creates a connection to the Azure DevOps organization using the provided 
credentials and project.
"""
class WorkItemManager:
    def __init__(self, org_url, personal_access_token, project_name):
        self.organization_url = org_url
        self.personal_access_token = personal_access_token
        self.project_name = project_name
        self.connection = self._create_connection()

    def _create_connection(self):
        credentials = BasicAuthentication('', self.personal_access_token)
        return Connection(base_url=self.organization_url, creds=credentials)

    def _chunk_list(self, lst, chunk_size):
        for i in range(0, len(lst), chunk_size):
            yield lst[i:i + chunk_size]

    #@profile_func
    def fetch_work_item_details(self, ids, wit_client):
        try:
            work_items_data = wit_client.get_work_items(ids=ids, expand='All')
            return work_items_data
        except Exception as e:
            logger.error(f"Error fetching work item details for IDs {ids}: {e}")
            return []

    def query_work_items(self, wiql_query, max_items=None, max_workers=300, chunk_size=50):
        logger.info("Querying Azure DevOps for work items...")
        wit_client = self.connection.clients.get_work_item_tracking_client()
        query_result = wit_client.query_by_wiql(Wiql(query=wiql_query))
        work_item_references = query_result.work_items
        process = psutil.Process(os.getpid())

        if max_items is not None:
            work_item_references = work_item_references[:max_items]
        ids = [ref.id for ref in work_item_references]
        ids_chunks = list(self._chunk_list(ids, chunk_size=chunk_size))
        total_chunks = len(ids_chunks)

        work_items = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_chunk = {executor.submit(self.fetch_work_item_details, chunk, wit_client): i for i, chunk in enumerate(ids_chunks, 1)}

            for future in as_completed(future_to_chunk):
                chunk_index = future_to_chunk[future]
                try:
                    data = future.result()
                    work_items.extend([WorkItem(work_item_data=item, organization_url=self.organization_url, project_name=self.project_name) for item in data])
                except Exception as exc:
                    logger.error(f'Chunk {chunk_index} generated an exception: {exc}')

        return work_items

    def fetch_related_work_item_details(self, related_work_item_id, wit_client):
        try:
            # Start processing a related work item
            related_work_item_data = wit_client.get_work_item(related_work_item_id, expand='All')
            return WorkItem(work_item_data=related_work_item_data, organization_url=self.organization_url, project_name=self.project_name)
        except Exception as e:
            logger.error(f"Error fetching related work item details for ID {related_work_item_id}: {e}")
            return None

    def fetch_related_work_items(self, work_item_id, max_workers=300, chunk_size=100):
        # Initialize an empty list to hold the fetched related WorkItem objects.
        related_work_items = []

        # Obtain a client for interacting with Azure DevOps work item tracking services.
        wit_client = self.connection.clients.get_work_item_tracking_client()

        # Fetch the specified work item, including its relations, from Azure DevOps.
        work_item = wit_client.get_work_item(work_item_id, expand='Relations')

        # Check if the work item has any relations.
        if work_item.relations:
            # Extract the IDs of related work items, filtering for specific relation types that
            # indicate hierarchical or related links.
            related_work_item_ids = [int(relation.url.split('/').pop()) for relation in work_item.relations if relation.rel in ['System.LinkTypes.Hierarchy-Forward', 'System.LinkTypes.Related']]
            
            # Count the total number of related work items to be fetched.
            total_related_items = len(related_work_item_ids)

            # Chunk the list of related work item IDs into smaller lists of size `chunk_size`.
            ids_chunks = self._chunk_list(related_work_item_ids, chunk_size)

            # Use a ThreadPoolExecutor to fetch the details of each chunk of related work items concurrently,
            # limiting the maximum number of concurrent threads to `max_workers`.
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Submit asynchronous tasks to the executor for fetching each chunk of related work item details.
                futures = {executor.submit(self.fetch_work_item_details, chunk, wit_client) for chunk in ids_chunks}

                # Initialize a counter for the number of related work items fetched so far.
                completed = 0

                # Wait for each asynchronous task to complete and process its result.
                for future in as_completed(futures):
                    # Retrieve the result of the task, which is a batch of related WorkItem objects.
                    related_work_items_batch = future.result()

                    # If the batch is not empty, extend the main list of related work items with the batch,
                    # and update the count of completed items.
                    if related_work_items_batch:
                        related_work_items.extend(related_work_items_batch)
                        completed += len(related_work_items_batch)

        # Return the list of fetched related WorkItem objects.
        return related_work_items
