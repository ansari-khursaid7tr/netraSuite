import subprocess
import shutil
import socket
import requests
from rich.console import Console

console = Console()


def is_port_open(host: str, port: int) -> bool:
    """Check if Ollama is already serving on localhost:11434"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        return sock.connect_ex((host, port)) == 0


def install_tool(tool: str, install_cmd: str):
    if shutil.which(tool) is None:
        console.print(f"[yellow]Installing {tool}...[/yellow]")
        try:
            subprocess.run(install_cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            console.print(f"[red]❌ Failed to install {tool}. Please install it manually.[/red]")
    else:
        console.print(f"[green]✔ {tool} is already installed.[/green]")


def install_ollama():
    if shutil.which("ollama") is None:
        console.print("[yellow]Installing Ollama...[/yellow]")
        subprocess.run("curl -fsSL https://ollama.com/install.sh | sh", shell=True, check=True)
    else:
        console.print("[green]✔ Ollama is already installed.[/green]")


def start_ollama_server():
    if is_port_open("localhost", 11434):
        console.print("[green]✔ Ollama server is already running.[/green]")
    else:
        console.print("[blue]🚀 Starting Ollama server in background...[/blue]")
        subprocess.Popen(["ollama", "serve"])


def pull_model_if_needed(model="mistral"):
    try:
        response = requests.get("http://localhost:11434/api/tags")
        response.raise_for_status()
        installed_models = [m["name"] for m in response.json()["models"]]
        if model in installed_models:
            console.print(f"[green]✔ Model '{model}' is already pulled.[/green]")
            return
    except Exception:
        console.print("[red]⚠ Could not verify installed models. Trying to pull anyway.[/red]")

    console.print(f"[yellow]📦 Pulling model '{model}'...[/yellow]")
    subprocess.run(f"ollama pull {model}", shell=True, check=True)


def main():
    console.print("[bold cyan]🔧 NetraSuite Environment Setup[/bold cyan]")

    # Replaced toolchain
    install_tool("nmap", "sudo apt install -y nmap")
    install_tool("masscan", "sudo apt install -y masscan")
    install_tool("ncrack", "sudo apt install -y ncrack")
    install_tool("dnsenum", "sudo apt install -y dnsenum")
    install_tool("whois", "sudo apt install -y whois")
    install_tool("dig", "sudo apt install -y dnsutils || sudo apt install -y bind9-dnsutils")

    # httpx typically comes via Go
    if shutil.which("httpx") is None:
        console.print("[yellow]Installing httpx using Go...[/yellow]")
        try:
            subprocess.run("go install github.com/projectdiscovery/httpx/cmd/httpx@latest", shell=True, check=True)
            console.print("[green]✔ httpx installed. Add $GOPATH/bin to your PATH if not already.[/green]")
        except Exception:
            console.print("[red]❌ Failed to install httpx. Please ensure Go is installed.[/red]")
    else:
        console.print("[green]✔ httpx is already installed.[/green]")

    install_ollama()
    start_ollama_server()
    pull_model_if_needed("mistral")

    console.print("[bold green]✅ All done! NetraSuite is ready to go.[/bold green]")


if __name__ == "__main__":
    main()
