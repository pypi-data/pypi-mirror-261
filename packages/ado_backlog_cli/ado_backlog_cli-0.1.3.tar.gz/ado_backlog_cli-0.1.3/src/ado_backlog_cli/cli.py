"""
Command line interface for interacting with Azure DevOps work items.

Provides commands for fetching work items, listing late work items,
and getting the work item schema.

The CLI stores state such as fetched work items in the click context
object, which is passed between commands.
"""

# Import necessary modules
import click  
import os
from .config import load_config
from .log_config import setup_logging
from . import work_item_utils as wiu
import logging

# Create click group and pass context object
@click.group()
@click.option('--log-level', default='INFO', help='Set the log level.')  
@click.pass_context
def cli(ctx, log_level):
    
    # Initialize context object
    ctx.ensure_object(dict)
    
    # Set log level
    ctx.obj['LOG_LEVEL'] = log_level.upper()
    
    # Set up logging
    setup_logging(log_level=ctx.obj['LOG_LEVEL'])
    
    # Initialize context object if needed
    if ctx.obj is None:
        ctx.obj = {}
        
    try:
        # Load config
        ctx.obj['config'] = load_config()
        
        # Get PAT from environment
        ctx.obj['pat'] = os.getenv('ADO_PAT')
        
        # Check if PAT is missing
        if not ctx.obj['pat']:
            click.echo("Error: Personal Access Token (PAT) not found in environment variable 'ADO_PAT'", err=True)
            ctx.exit(1)
            
    except Exception as e:
        # Handle errors
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)
        
# Command to fetch work items        
@cli.command(name='fetch-work-items', help="Fetch work items from Azure DevOps.")
@click.option('--max-items', default=None, type=int, help='Maximum number of work items to fetch. If not specified, all items are fetched.')
@click.pass_context
def fetch_work_items(ctx, max_items):
    
    # Fetch and process work items
    work_items = wiu.fetch_and_process_work_items(ctx.obj['config'], ctx.obj['pat'], max_items)
    
    # Store in context
    ctx.obj['work_items'] = work_items
    
# Command to list late work items
@cli.command(name='list-late-work-items', help="List work items that are late.")
@click.pass_context
def list_late_work_items(ctx):
    
    # Check if work items have been fetched
    if 'work_items' not in ctx.obj or not ctx.obj['work_items']:
        click.echo("Please fetch work items first using the 'fetch-work-items' command.")
        return
        
    # Filter late work items
    late_work_items = wiu.filter_late_work_items(ctx.obj['work_items'])
    
    # Output late work items
    for work_item in late_work_items:
        click.echo(work_item.summary())
        
# Command to get work item schema        
@cli.command(name='get-schema', help="Get the schema of work items.")
@click.pass_context
def get_schema(ctx):

    # Check if work items have been fetched
    if 'work_items' not in ctx.obj or not ctx.obj['work_items']:
        click.echo("Please fetch work items first using the 'fetch-work-items' command.")
        return

    # Get schema
    schema = wiu.get_work_item_schema(ctx.obj['work_items'])
    
    # Output schema
    click.echo(schema)

if __name__ == '__main__':
    cli(obj={})
