import os
import re
import yaml
import logging

logger = logging.getLogger(__name__)

# Function to ensure config path exists
def ensure_config_path():
    """
    Ensure the configuration directory and file exist.
    Creates them if they do not exist.
    """
    config_dir = os.path.expanduser('~/.config/ado-backlog-cli')
    config_path = os.path.join(config_dir, 'config.yml')

    # Create the directory if it does not exist
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # Create a blank config file if it does not exist
    if not os.path.isfile(config_path):
        with open(config_path, 'w') as file:
            yaml.dump({}, file)  # Creates an empty YAML file

    return config_path

# Function to validate URL 
def is_valid_url(url):
    # Simple URL validation using regex
    return re.match(r'https?://[^\s]+', url) is not None

# Function to load config and validate required fields
def load_config():
    """
    Load and return the configuration from a YAML file,
    ensuring it contains specific required fields with valid values,
    and handles backslashes in iteration_path.

    Returns:
        dict: The configuration as a dictionary, with iteration_path processed.
    """
    
    # Ensure config path exists and get path
    config_path = ensure_config_path()  

    # Check if config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file does not exist: {config_path}")

    # Load config file
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file) or {}  # Handle empty config

    # Validate required azure_devops section and keys
    azure_devops_required_keys = ['org_url', 'project_name', 'iteration_path']
    missing_keys = [key for key in azure_devops_required_keys if key not in config.get('azure_devops', {})]

    # Raise error if any required keys are missing
    if missing_keys:
        raise ValueError(f"""
Your config file seems to be missing some key information under 'azure_devops': {', '.join(missing_keys)}.

Please ensure your config file at {config_path} includes 'org_url', 'project_name', and 'iteration_path' under 'azure_devops'.

Here's an example of what it might look like:

    azure_devops:
      org_url: "https://your-organization.visualstudio.com/"  
      project_name: "Your Project Name"
      iteration_path: "Your\\Project\\Path"

Note:
- The 'iteration_path' should use double backslashes (\\\\) for correct escaping.
- Ensure that 'org_url' is a valid URL.
- 'project_name' should be a string.

""")
    
    # Get azure_devops config section
    azure_devops = config['azure_devops']

    # Validate org_url is valid URL
    if not is_valid_url(azure_devops['org_url']):
        raise ValueError(f"Invalid org_url: {azure_devops['org_url']}")

    # Validate project_name is string
    if not isinstance(azure_devops['project_name'], str):
        raise ValueError("project_name must be a string.")

    # Process iteration_path - replace '\' with '\\'
    iteration_path = azure_devops['iteration_path'].replace('\\', '\\\\')
    azure_devops['iteration_path'] = iteration_path

    return config
