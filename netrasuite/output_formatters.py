from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()


def display_nmap_output(output: str, resolved_target: str = None):
    lines = output.splitlines()
    ports = []
    scanned_ip = "Unknown"
    latency = "Unknown"
    mac_address = "Unknown"

    for line in lines:
        if "Nmap scan report for" in line:
            scanned_ip = line.split()[-1]
        elif "Host is up" in line:
            latency = line.split("(")[-1].replace(" latency).", "").strip()
        elif "/tcp" in line and "open" in line:
            parts = line.split()
            port = parts[0]
            state = parts[1]
            service = parts[2]
            version = " ".join(parts[3:]) if len(parts) > 3 else "-"
            ports.append((port, state, service, version))
        elif "MAC Address:" in line:
            mac_address = line.split("MAC Address:")[1].strip()

    domain_info = (
        f"{resolved_target} ({scanned_ip})"
        if resolved_target and resolved_target != scanned_ip and scanned_ip != "Unknown"
        else scanned_ip
    )

    console.print("\n[bold green]✔ Nmap Scan Complete[/bold green]")
    console.print(
        Panel(
            f"[white]Target:[/white] {domain_info}\n"
            f"[white]Host Status:[/white] Up ({latency} latency)\n"
            f"[white]MAC Address:[/white] {mac_address}",
            title="Host Summary",
            expand=False,
        )
    )

    if ports:
        table = Table(title="Open Ports")
        table.add_column("Port", style="cyan", justify="right")
        table.add_column("State", style="green")
        table.add_column("Service", style="magenta")
        table.add_column("Version", style="white")
        for port, state, service, version in ports:
            table.add_row(port, "🟢 open" if state == "open" else "🔴 closed", service, version)
        console.print(table)
    else:
        console.print("[yellow]No open ports found or parsing failed.[/yellow]")


def display_whois_output(output: str):
    console.print("[bold green]✔ WHOIS Lookup Result[/bold green]")
    #syntax = Syntax(output, "text", theme="ansi_dark", line_numbers=False)
    console.print(output)


def display_dig_output(output: str):
    console.print("[bold green]✔ DNS Lookup (dig)[/bold green]")
    #syntax = Syntax(output, "text", theme="paraiso-dark", line_numbers=False)
    console.print(output)
