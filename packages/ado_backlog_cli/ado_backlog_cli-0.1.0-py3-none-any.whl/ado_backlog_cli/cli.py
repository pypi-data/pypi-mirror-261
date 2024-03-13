# src/pythia/cli.py
import click
import logging
from .cli_argument_parser import CLIArgumentParser


# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@click.group()
def cli():
    """Pythia CLI: A tool to make sense of ADO Backlogs for reports."""
    pass

# Register the command from CLIArgumentParser
cli.add_command(CLIArgumentParser.fetch_work_items())

if __name__ == '__main__':
    cli()
