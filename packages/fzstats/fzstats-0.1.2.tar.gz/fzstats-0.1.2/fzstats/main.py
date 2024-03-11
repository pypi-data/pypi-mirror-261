import os
from dataclasses import dataclass
from enum import Enum
from typing import Annotated, Literal

import typer
from rich.console import Console
from rich.table import Column, Table

app = typer.Typer()


@dataclass
class PathSize:
    name: str
    type: Literal["file", "folder"]
    size: int


class SortBy(Enum):
    NAME = "name"
    TYPE = "type"
    SIZE = "size"


class SortDirection(Enum):
    DESC = "desc"
    ASC = "asc"


def get_folder_size(folder_path="."):
    """Get folder size

    Args:
        folder_path (str, optional): path to the folder. Defaults to '.'.

    Returns:
        int: folder size in bytes
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def get_children_sizes(
    folder_path: str = ".",
    sort_by: str = "size",
    sort_dir: Literal["asc", "desc"] = "desc",
    limit: int = None,
) -> list[PathSize]:
    """Get folder children sizes

    Args:
        folder_path (str, optional): The path to the folder. Defaults to ".".
        sort_by (str, optional): Sort results by. Defaults to "size".
        sort_dir (str, optional): Sort direction. Defaults to "desc".
        limit (int, optional): limit results by. Defaults to "None".

    Returns:
        list[PathSize]: folder children with their sizes
    """
    children_with_sizes = []
    for child in os.listdir(folder_path):
        child_path = os.path.join(folder_path, child)

        if os.path.isfile(child_path):
            size = os.path.getsize(child_path)
            children_with_sizes.append(PathSize(child, "file", size))
        elif os.path.isdir(child_path):
            size = get_folder_size(child_path)
            children_with_sizes.append(PathSize(child, "folder", size))

    reverse = sort_dir == "desc"
    children_with_sizes.sort(key=lambda item: getattr(item, sort_by), reverse=reverse)

    if limit:
        children_with_sizes = children_with_sizes[0:limit]
    return children_with_sizes


def format_size(size: int) -> str:
    one_kb = 1024
    one_mb = 1024**2
    one_gb = 1024**3
    if size > one_gb:
        return f"{size / one_gb:.1f}G"
    if size > one_mb:
        return f"{size / one_mb:.1f}M"
    if size > one_kb:
        return f"{size / one_kb:.1f}K"
    return f"{size}B"


def limit_callback(value: int):
    if value and value <= 0:
        raise typer.BadParameter("Only positive values are allowed")
    return value


@app.command()
def main(
    folder_path: Annotated[str, typer.Argument(help="The path to the folder.")] = ".",
    sort_by: Annotated[
        SortBy,
        typer.Option("--sort", "-s", help="Sort the results by a specific attribute."),
    ] = "size",
    sort_dir: Annotated[
        SortDirection, typer.Option("--dir", "-d", help="Sort direction.")
    ] = "desc",
    limit: Annotated[
        int,
        typer.Option(
            "--limit",
            "-l",
            callback=limit_callback,
            help="Limit the results to a given number of rows.",
        ),
    ] = None,
):
    children_with_sizes = get_children_sizes(
        folder_path, sort_by.value, sort_dir.value, limit
    )
    table = Table(
        "Name",
        Column("Size", justify="right", style="green"),
    )
    for item in children_with_sizes:
        name = item.name if item.type == "file" else f"[blue]{item.name}"
        table.add_row(name, format_size(item.size))

    console = Console()
    console.print(table)
