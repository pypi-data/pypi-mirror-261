from work_item_manager import WorkItemManager
import os

def main():
    # Setup Azure DevOps credentials and project details
    personal_access_token = os.getenv('ADO_PAT')  # It's recommended to use an environment variable for your PAT
    organization_url = 'https://geico.visualstudio.com/'
    project_name = 'Observability'


    # Ensure you replace YOUR_ORGANIZATION and YOUR_PROJECT_NAME with your actual Azure DevOps organization and project name.
    # The personal access token (PAT) should have sufficient permissions to read work items.

    # Define your WIQL query
    wiql_query = """
    SELECT [System.Id], [System.Title], [System.State] FROM WorkItems 
    WHERE [System.TeamProject] = @project 
    AND [System.WorkItemType] = 'Bug'
    AND [System.State] <> 'Closed'
    ORDER BY [System.CreatedDate] DESC
    """

    # Initialize WorkItemManager and query work items
    work_item_manager = WorkItemManager(organization_url, personal_access_token, project_name)
    work_items = work_item_manager.query_work_items(wiql_query)

    # Print summary for each retrieved work item
    for work_item in work_items:
        print(work_item.summary())

if __name__ == "__main__":
    main()
