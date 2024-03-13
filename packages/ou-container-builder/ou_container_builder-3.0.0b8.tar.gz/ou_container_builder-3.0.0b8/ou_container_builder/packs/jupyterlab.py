"""Functionality to install JupyterLab."""

from pydantic import BaseModel
from typing import Literal

from rich.progress import Progress

from ou_container_builder.state import State
from ou_container_builder.util import docker_run_cmd

name = "jupyterlab"


class Options(BaseModel):
    """Options for the JupyterLab pack."""

    version: Literal[4] = 4
    announcements: bool = False


def init(state: State) -> None:
    """Initialise packs.jupyterlab."""
    if state["packs"]["jupyterlab"]["version"] == 4:
        state.update({"packages": {"pip": {"system": ["jupyterlab>=4.0.2,<5"]}}})
    if not state["packs"]["jupyterlab"]["announcements"]:
        state.update(
            {
                "output_blocks": {
                    "deploy": [
                        {
                            "block": docker_run_cmd(
                                [
                                    '/var/lib/ou/python/system/bin/jupyter labextension disable "@jupyterlab/apputils-extension:announcements"'
                                ]
                            ),
                            "weight": 1001,
                        }
                    ]
                }
            }
        )


def generate(state: State, progress: Progress) -> None:
    """Unused."""
    pass
