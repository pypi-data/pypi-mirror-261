import os
import yaml

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

def load_config():
    """
    Load and return the configuration from a YAML file, 
    with specific handling for backslashes in iteration_path.

    Returns:
        dict: The configuration as a dictionary, with iteration_path processed.
    """
    config_path = ensure_config_path()  # Ensure config path and get the config file path

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file does not exist: {config_path}")
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file) or {}  # Handle empty config

    # Process the iteration_path to handle backslashes safely
    if 'azure_devops' in config and 'iteration_path' in config['azure_devops']:
        iteration_path = config['azure_devops']['iteration_path']
        iteration_path = iteration_path.replace('\\', '\\\\')
        # Update the configuration with the processed path
        config['azure_devops']['iteration_path'] = iteration_path
    
    return config

# Example usage
if __name__ == "__main__":
    try:
        config = load_config()
        print(config)  # Process the config as needed
    except FileNotFoundError as e:
        print(e)
