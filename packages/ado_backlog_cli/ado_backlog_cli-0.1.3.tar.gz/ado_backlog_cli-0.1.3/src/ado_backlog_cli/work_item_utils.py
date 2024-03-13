import logging
from .work_item_manager import WorkItemManager
from pympler import asizeof
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

logger = logging.getLogger(__name__)

def fetch_and_process_work_items(config, personal_access_token, max_items=None):
    logger.info("Starting to fetch work items...")
    org_url = config['azure_devops']['org_url']
    project_name = config['azure_devops']['project_name']

    manager = WorkItemManager(org_url=org_url, personal_access_token=personal_access_token, project_name=project_name)

    wiql_query = f"""
    SELECT [System.Id], [System.Title], [System.State]
    FROM WorkItems
    WHERE [System.TeamProject] = '{project_name}'
    ORDER BY [System.CreatedDate] DESC
    """
    try:
        work_items = manager.query_work_items(wiql_query, max_items)
        if work_items is None:
            logger.info("No work items found.")
            return []

        # This will hold both primary and related work items
        all_work_items = list(work_items)  # Start with the initially fetched work items

        # Use ThreadPoolExecutor to fetch related work items concurrently
        with ThreadPoolExecutor() as executor:
            # Submit a future for each work item to fetch its related items
            future_to_work_item = {executor.submit(manager.fetch_related_work_items, work_item.id): work_item for work_item in work_items}

            for future in as_completed(future_to_work_item):
                work_item = future_to_work_item[future]
                try:
                    related_items = future.result()  # Get the result of fetching related items
                    all_work_items.extend(related_items)  # Add related work items to the list
                except Exception as e:
                    logger.error(f"Error fetching related items for work item {work_item.id}: {e}")

        logger.info(f"Fetched {len(all_work_items)} work items including related items.")
        logger.info(f"Results from ADO is: {asizeof.asizeof(all_work_items) / 1000000} megabytes.")
        return all_work_items
    except Exception as e:
        logger.error(f"Error fetching work items: {e}")
        return []

def filter_late_work_items(work_items):
    late_work_items = []

def get_work_item_schema(work_items):
    """
    Inspects the given list of WorkItem objects to deduce the schema of a work item.
    Assumes all work items follow the same schema.

    Args:
        work_items (list of WorkItem): The list of WorkItem objects to inspect.

    Returns:
        dict: A dictionary representing the schema of a work item, with keys and their value types.
    """
    if not work_items:
        logger.info("No work items provided for schema deduction.")
        return {}

    # Use the first work item as a sample for schema deduction
    sample_item = work_items[0]
    schema = {"id": type(sample_item.id).__name__}

    for key, value in sample_item.data.items():
        schema[key] = type(value).__name__

    # Adding fixed attributes of WorkItem class beyond dynamic data
    schema.update({
        "organization_url": type(sample_item.organization_url).__name__,
        "project_name": type(sample_item.project_name).__name__,
        "hyperlink": "str"  # Assuming hyperlink is always a string
    })

    return schema
