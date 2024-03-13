import logging

logger = logging.getLogger(__name__)

class WorkItem:
    def __init__(self, work_item_data, organization_url, project_name):
        """
        Initializes a WorkItem instance with data and configuration.

        Args:
            work_item_data: The data retrieved from Azure DevOps for a single work item.
                            This is expected to be an object, not a dictionary.
            organization_url (str): The URL of the Azure DevOps organization.
            project_name (str): The name of the Azure DevOps project.
        """
        # Assuming work_item_data is an object, access its attributes directly
        self.id = getattr(work_item_data, 'id', None)
        self.data = getattr(work_item_data, 'fields', {})
        logger.debug(f"Work item data: {self.data}")

        self.organization_url = organization_url
        self.project_name = project_name

    @property
    def title(self):
        return self.data.get('System.Title', 'N/A')[:80]

    @property
    def state(self):
        return self.data.get('System.State')

    @property
    def hyperlink(self):
        return f"{self.organization_url}/{self.project_name}/_workitems/edit/{self.id}"

    def summary(self):
        return f"ID {self.id}: {self.title} (State: {self.state})"
