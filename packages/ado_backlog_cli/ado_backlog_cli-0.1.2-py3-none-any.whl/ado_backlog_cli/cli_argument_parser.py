import click
import logging
from .work_item_manager import WorkItemManager
from .config import load_config
from pympler import asizeof

logger = logging.getLogger(__name__)

class CLIArgumentParser:
    @staticmethod
    def fetch_work_items():
        config = load_config()

        @click.command(name='fetch-work-items', help="Fetch work items from Azure DevOps.")
        @click.option('--pat', envvar='ADO_PAT', prompt=True, hide_input=True, required=False, default=None, help='Your Personal Access Token for Azure DevOps.')
        @click.option('--max-items', default=None, type=int, help='Maximum number of work items to fetch. If not specified, all items are fetched.')
        def command(pat, max_items):
            logger.info("Starting to fetch work items...")
            org_url = config['azure_devops']['org_url']
            project_name = config['azure_devops']['project_name']

            manager = WorkItemManager(org_url=org_url, personal_access_token=pat, project_name=project_name)
            
            wiql_query = """
            SELECT [System.Id], [System.Title], [System.State]
            FROM WorkItems
            WHERE [System.TeamProject] = '{}'
            ORDER BY [System.CreatedDate] DESC
            """.format(project_name)

            work_items = manager.query_work_items(wiql_query, max_items)
            logger.info(f"Fetched {len(work_items)} work items.")
            logger.info(f"Results from ADO is: {asizeof.asizeof(work_items) / 1000000} megabytes.")

            #for work_item in work_items:
            #    click.echo(work_item.summary())
        
        return command
