import yaml
import os

def load_config(config_path='config.yml'):
    """
    Load and return the configuration from a YAML file, 
    with specific handling for backslashes in iteration_path.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: The configuration as a dictionary, with iteration_path processed.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file does not exist: {config_path}")
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

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
