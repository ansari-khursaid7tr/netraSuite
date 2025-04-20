from netrasuite.llm import query_ollama
from netrasuite.command_executor import run_command
from netrasuite.output_formatters import (
    display_nmap_output,
    display_whois_output,
    display_dig_output,
)
from rich.console import Console
from pyfiglet import Figlet
from rich.panel import Panel
from rich.text import Text
import socket
import re
import os
import readline
import atexit
from rich.spinner import Spinner
from netrasuite.__version__ import __version__, __creator__

console = Console()
HISTORY_FILE = os.path.expanduser("~/.netrasuite_history")

if os.path.exists(HISTORY_FILE):
    readline.read_history_file(HISTORY_FILE)

atexit.register(lambda: readline.write_history_file(HISTORY_FILE))

PROMPT = "\033[94mnetrasuite > \033[0m"

def pre_input_hook():
    readline.insert_text("")
    readline.redisplay()

readline.set_pre_input_hook(pre_input_hook)

def resolve_host_to_ip(command: str):
    domain_to_ip = {}
    # Only resolve IP if the tool requires it
    ip_tools = ["nmap", "masscan", "ncrack"]  # tools that need IPs
    domain_tools = ["dnsenum", "httpx", "whois", "dig", "dnsrecon"]  # tools that require domain

    # Extract first word of command to identify tool
    parts = command.strip().split()
    if not parts:
        return command, domain_to_ip

    tool = parts[0].lower()

    # Don't modify if domain-based tool
    if tool in domain_tools:
        return command, domain_to_ip

    # Otherwise, resolve domain names to IPs
    pattern = r"\b([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|localhost)\b"
    matches = re.findall(pattern, command)
    for domain in matches:
        try:
            ip = "127.0.0.1" if domain == "localhost" else socket.gethostbyname(domain)
            command = command.replace(domain, ip)
            domain_to_ip[ip] = domain
        except socket.gaierror:
            continue

    return command, domain_to_ip

def print_banner():
    fig = Figlet(font="slant")
    ascii_logo = fig.renderText("NetraSuite")
    console.print("[white]" + "─" * 60 + "[/white]")
    console.print(f"[bold green]{ascii_logo}[/bold green]")
    console.print(Text("\t\t\t\t\t\t\t v{}".format(__version__), style="bold magenta", justify="right"))
    console.print(Text("\t\t\t     LLM-Powered Network Assistant Tool", style="bold cyan", justify="right"))
    console.print(Text("Starting NetraSuite ...", style="bold blue"), justify="left")
    console.print("[white]" + "─" * 60 + "[/white]")

def detect_tool(command: str):
    if command.startswith("nmap"):
        return "nmap"
    elif command.startswith("whois"):
        return "whois"
    elif command.startswith("dig"):
        return "dig"
    else:
        return "unknown"

def clear_ollama_sessions():
    ollama_dir = os.path.expanduser("~/.ollama")
    targets = ["sessions", "tmp", "cache"]
    for t in targets:
        path = os.path.join(ollama_dir, t)
        if os.path.exists(path):
            try:
                import shutil
                shutil.rmtree(path)
                console.print(f"[cyan]Cleared: {t}[/cyan]")
            except Exception as e:
                console.print(f"[red]Failed to clear {t}: {e}[/red]")

def print_help():
    print("""
NetraSuite is a terminal-based assistant that uses local LLMs to convert natural language
network security queries into real tool commands (nmap, zeek, tshark, nfdump).

🔹 Example Prompts:
  - scan localhost for open ports and running services
  - scan the domain tesla.com from port 20 to 443
  - get A record of google.com
  - perform whois lookup on google.com
  - find MX and TXT records of facebook.com
  - who owns the domain google.com
  

🔹 Built-in Commands:
  • help      → show this message
  • clear     → clear the screen
  • restart   → restart the tool
  • exit/quit → close the tool
  • /bye      → close the tool
  

🔹 Tips:
  - You don’t need to know the exact command syntax
  - You can refer to domains (like google.com) and they’ll resolve automatically
  - Tool selection is automatic based on what you ask
    """)

def print_about():
    print(f"""
NetraSuite v{__version__}
LLM-Powered Network Security Assistant Tool

Created by: {__creator__}
Built on: Python 3, Rich, and local LLMs via Ollama
Purpose: Automate infosec tools using natural language prompts.
    """)

def main():
    print_banner()
    try:
        while True:
            raw = input(PROMPT)
            prompt = raw.strip().lower()
            readline.add_history(prompt)

            if prompt in ["exit", "quit", "/bye"]:
                console.print("[red]Exiting NetraSuite...[/red]")
                clear_ollama_sessions()
                break
            elif prompt == "clear":
                os.system("clear")
                clear_ollama_sessions()
                continue
            elif prompt == "about":
                print_about()
                continue
            elif prompt == "restart":
                os.system("clear")
                clear_ollama_sessions()
                main()
            elif prompt in ["help", "hello"]:
                print_help()
                continue

            with console.status("[bold cyan]Generating command...[/bold cyan]", spinner="dots"):
                original_command = query_ollama(prompt)

            interpreted, domain_map = resolve_host_to_ip(original_command)
            console.print(f"[yellow]Interpreted Command:[/yellow] {interpreted}")
            output = run_command(interpreted)
            tool = detect_tool(interpreted)

            if tool == "nmap":
                target_ip = interpreted.split()[-1]
                resolved_name = domain_map.get(target_ip, None)
                display_nmap_output(output, resolved_target=resolved_name)
            elif tool == "whois":
                display_whois_output(output)
            elif tool == "dig":
                display_dig_output(output)
            else:
                console.print(output)

    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
