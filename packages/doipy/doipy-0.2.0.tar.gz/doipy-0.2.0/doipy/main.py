import typer
from typing import Annotated

from doipy.actions import create, create_fdo, hello, list_operations, search

app = typer.Typer()


@app.command(name='create')
def create_command(files: Annotated[list[typer.FileBinaryRead], typer.Argument(help='A list of files for an FDO.')],
                   md_file: Annotated[
                       str, typer.Option(help='Name of the file containing metadata in JSON format')
                   ] = None,
                   client_id: Annotated[str, typer.Option(help='The identifier of the user in Cordra')] = None,
                   password: Annotated[str, typer.Option(help='Password of the user')] = None):
    """Create a new Digital Object (DO) from input files."""
    do_type = 'Document'
    create(do_type, files, md_file, client_id, password)


@app.command(name='create_fdo')
def create_fdo_command(data_ref: Annotated[str, typer.Argument(help='The identifier of the data object')],
                       md_ref: Annotated[str, typer.Argument(help='The identifier of the metadata object')],
                       client_id: Annotated[str, typer.Option(help='The identifier of the user in Cordra')] = None,
                       password: Annotated[str, typer.Option(help='Password of the user')] = None):
    """Create a new FAIR Digital Object (FDO) from data and metadata references."""
    create_fdo(data_ref, md_ref, client_id, password)


@app.command(name='hello')
def hello_command(username: Annotated[str, typer.Argument(help='username')],
                  password: Annotated[str, typer.Argument(help='password')]):
    """Say hello!"""
    hello(username, password)


@app.command(name='list_operations')
def list_operations_command(target_id: Annotated[str, typer.Option(help='target_id')] = None,
                            client_id: Annotated[str, typer.Option(help='client_id')] = None,
                            password: Annotated[str, typer.Option(help='password')] = None):
    """List all available operations."""
    list_operations(target_id, client_id, password)


@app.command(name='search')
def search_command(query: Annotated[str, typer.Argument(help='query')],
                   username: Annotated[str, typer.Option(help='username')] = None,
                   password: Annotated[str, typer.Option(help='password')] = None):
    """Search with a query."""
    search(query, username, password)
