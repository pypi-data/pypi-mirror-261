import os
from pathlib import Path
import click
from click import option, group
from stony import Stony, Config, Client, load_config


@group()
def cli():
    "Static site generator powered by Notion"


@cli.command
@option(
    "--out",
    "-o",
    default="dist",
    help="Directory to build the site. Default `dist`",
    type=click.Path(path_type=Path),
)
@option(
    "--project-dir",
    default=os.getcwd(),
    help="Directory containg the stony project",
    type=click.Path(path_type=Path),
    envvar="STONY_PROJECT_DIR",
)
def build(out, project_dir):
    """
    Build the site
    """

    config = load_config(project_dir)
    client = Client()
    stony = Stony(client=client, config=config)
    print(f"Building into {out}")
    stony.build(out)
