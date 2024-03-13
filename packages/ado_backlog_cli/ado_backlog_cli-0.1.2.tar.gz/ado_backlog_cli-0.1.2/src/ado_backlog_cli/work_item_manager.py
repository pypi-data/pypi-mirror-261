import logging
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.work_item_tracking.models import Wiql
from concurrent.futures import ThreadPoolExecutor, as_completed

# Assuming WorkItem class exists as per your setup
from .work_item import WorkItem

logger = logging.getLogger(__name__)

class WorkItemManager:
    def __init__(self, org_url, personal_access_token, project_name):
        """
        Initializes a WorkItemManager instance to manage work items in Azure DevOps.
        """
        self.organization_url = org_url
        self.personal_access_token = personal_access_token
        self.project_name = project_name
        self.connection = self._create_connection()

    def _create_connection(self):
        """
        Creates a connection to the Azure DevOps organization.
        """
        credentials = BasicAuthentication('', self.personal_access_token)
        return Connection(base_url=self.organization_url, creds=credentials)

    def _chunk_list(self, lst, chunk_size):
        """Yield successive chunk_size chunks from lst."""
        for i in range(0, len(lst), chunk_size):
            yield lst[i:i + chunk_size]

    def fetch_work_item_details(self, ids, wit_client):
        """Fetch details for a batch of work item IDs."""
        try:
            work_items_data = wit_client.get_work_items(ids=ids, expand='All')
            return work_items_data
        except Exception as e:
            logger.error(f"Error fetching work item details for IDs {ids}: {e}")
            return []

    def query_work_items(self, wiql_query, max_items=None, max_workers=10, chunk_size=50):
        logger.info("Querying Azure DevOps for work items...")
        wit_client = self.connection.clients.get_work_item_tracking_client()
        query_result = wit_client.query_by_wiql(Wiql(query=wiql_query))
        
        work_item_references = query_result.work_items
        logger.info(f"Received {len(work_item_references)} work items from the query.")

        if max_items is not None:
            work_item_references = work_item_references[:max_items]

        # Chunking work item IDs for batch processing
        ids = [ref.id for ref in work_item_references]
        ids_chunks = self._chunk_list(ids, chunk_size=chunk_size)
        
        work_items = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_ids = {executor.submit(self.fetch_work_item_details, list(ids_chunk), wit_client): list(ids_chunk) for ids_chunk in ids_chunks}
            
            for future in as_completed(future_to_ids):
                ids_chunk = future_to_ids[future]
                try:
                    data = future.result()
                    for work_item_data in data:
                        work_item = WorkItem(work_item_data=work_item_data, 
                                             organization_url=self.organization_url, 
                                             project_name=self.project_name)
                        work_items.append(work_item)
                except Exception as exc:
                    logger.error(f'IDs {ids_chunk} generated an exception: {exc}')
                
        return work_items
