"""Helper functions for the celestical app"""

import json
from pathlib import Path
import os

import typer
import yaml

from pathlib import Path
from prettytable import PrettyTable, ALL
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()

welcome_message:str = "[purple]Direct deployment of containers or compose" \
                      +"files to a green cloud made by space engineers[/purple]"

# Service types definitions
#
# For each service type there is a list of keywords to detect them
SERVICE_TYPES = {
    "FRONTEND": ["web", "www", "frontend", "traefik", "haproxy", "apache", "nginx"],
    "API": ["api", "backend", "service"],
    "DB": ["database", "redis", "mongo", "mariadb", "postgre"],
    "BACKEND": ["hidden"]
}


# Building a table in the terminal
def create_empty_table(columns_labels):
    """Create an empty table with specified columns."""
    pt = PrettyTable()

    # Set the field names (columns)
    pt.field_names = columns_labels

    return pt


def add_row_to_table(table, row_dict):
    """Add a row to the table based on a dictionary."""
    if set(row_dict.keys()) != set(table.field_names):
        raise ValueError("Row dictionary keys do not match table columns.")
    table.add_row([row_dict[col] for col in table.field_names])


def cli_create_table(data: dict) -> Table:
    """Create a table from a dictionary.
    Params:
        data(dict): dictionary to be displayed
    Returns:
        (Table): table object
    """
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Key", style="dim")
    table.add_column("Value")

    for key, value in data.items():
        table.add_row(str(key), str(value))

    return table


def cli_panel(message: str, type="info") -> None:
    """Display a message in a panel.
    Params:
        message(str): message to be displayed
    Returns:
        None
    """

    # Note: here is hwo to join *args
    # buffer = "\n".join(str(arg) for arg in args)

    if type == "info":
        title = "Celestical CLI"
        panel = Panel(message, title=f"[bold purple]{title}[/bold purple]",
                    border_style="purple",
                    expand=True,
                    title_align='left')
    elif type == "error":
        title = "Celestical CLI Error"
        panel = Panel(message, title=f"[bold red]{title}[/bold red]",
            border_style="red",
            expand=True,
            title_align='left')


    console.print(panel)


def save_json(data: dict) -> bool:
    """Helper function to save the complete stack info.
    Params:
        data(dict): complete info about the stack (name, compose ..)
    Returns:

    """
    if "name" not in data:
        return False

    json_file = f'stack_{data["name"]}.json'
    try:
        with open(json_file, 'w') as jfile:
            json.dump(data, jfile, indent=4)
        print_text("Json saved successfully.")
        return True
    except Exception as e:
        print(f"Error: Unable to save data to f'stack_{data['name']}.json'")
        print(f'Error details: {e}')

    return False


def save_yaml(data: dict, yml_file:Path = None):
    """Helper function to save the complete stack info.
    Params:
        stack_info(dict): complete info about the stack (name, compose ..)
    Returns:

    """
    #yml_file = "docker-compose.yml"
    if yml_file is None:
        yml_file = Path("./docker-compose-enriched.yml")

    try:
        with yml_file.open(mode='w') as yfile:
            yaml.dump(data, yfile)
        print_text(f"YAML file created successfully: [green]{yml_file}[/green]")

    except Exception as e:
        print(f'Error: Unable to save data to {yml_file}')
        print(f'Error details: {e}')

    # return the Path object of the saved file
    return Path(yml_file)


def print_nested_dict(dictionary: dict):
    """Print a nested dictionary in a readable format."""
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print_nested_dict(value)
        else:
            print(f"{key}: {value}")


def print_feedback(used_input: str):
    """ Show users what they have input """
    console.print(f" :heavy_check_mark: - {used_input}")


def prompt_user(prompt: str, default:str = None) -> str:
    """Prompt the user for input.
    Params:
        prompt(str): the prompt text invitation
    Returns:
        str: the user input

    """
    resp = Prompt.ask(f"\n [yellow]===[/yellow] {prompt}", default=default)
    if resp is None:
        resp = ""
    return resp


def confirm_user(prompt: str, default:bool = True) -> str:
    """Prompt the user for yes no answer.
    Params:
        prompt(str): the prompt text invitation
    Returns:
        bool: the user confirmation
    """
    confirmation:bool = Confirm.ask(f"\n === {prompt} ", default=default)
    if confirmation is None:
        confirmation = False
    return confirmation


def print_text(text: str) -> str:
    """Print text to the CLI.
        Params:
            text(str): the text to print
        Returns:
            str: the text to print
    """
    return typer.echo(f"\n --- {text}")


def guess_service_type_by_name(service_name: str):
    """ Quick guess of service type
    """

    if len(service_name) == 0:
        return ""

    service_name = service_name.lower()

    for stype in SERVICE_TYPES:
        for guesser in SERVICE_TYPES[stype]:
            if guesser in service_name:
                return stype

    # if nothing found
    return ""

