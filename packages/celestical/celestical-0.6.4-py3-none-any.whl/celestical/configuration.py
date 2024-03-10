# Managing the configuration for the Celestical services
import json
import os
import logging
from pathlib import Path

import typer
from prettytable import PrettyTable, ALL

import celestical.api as api
from celestical.helper import print_text

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
apiconf = api.Configuration(
        host = "http://localhost:8000"
)

LOGGING_LEVEL = logging.INFO
logging.basicConfig(encoding='utf-8', level=LOGGING_LEVEL)

HOTLINE = "starship@celestical.net"

def get_default_config_path():
    """Return the default config path for this applications

    Returns:
        (str,str): directory of config file, absolut path to config file
    """
    path = Path.home() / ".config" / "celestical" / "config.json"
    return path


def load_config(config_path: str = "") -> dict:
    """Load config file from config_path.

    Params:
        config_path(str): non-default absolute path of the configuration.
    Returns:
        (dict): configuration content
    """
    path = get_default_config_path()
    if config_path is not None and config_path != "":
        path = Path(config_path)

    user_data = {}
    if path.exists():
        try:
            with open(path, 'r') as f_desc:
                user_data = json.load(f_desc)
        except:
            print_text("Could not read the configuration file.")
    else:
        print_text("The configuration file does not exist yet.")

    return user_data


def save_config(config:dict):
    """Save config file to the default_config_path.

    Params:
        config(dict): configuration.
    Returns:
        (str): configuration absolut path
    """
    cpath = get_default_config_path()

    try:
        if not cpath.parent.exists():
            os.makedirs(cpath.parent, exist_ok=True)
    except Exception as e:
        typer.echo("Config directory couldn't be created successfully")

    with open(cpath, 'w') as f:
        json.dump(config, f, indent=4)

    typer.echo(f"Login credentials stored safely in: {cpath}")
    return cpath
