import shutil
from rich.console import Console

console = Console()

def ensure_tools_exist(tools):
    for tool in tools:
        if not shutil.which(tool):
            console.print(f"[red]{tool} not found in PATH.[/red]")
        else:
            console.print(f"[green]{tool} is installed.[/green]")
