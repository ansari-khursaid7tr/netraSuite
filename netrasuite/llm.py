import requests
import re

def query_ollama(prompt: str, model: str = "mistral"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": (
            "Convert the following instruction into a SINGLE Linux terminal command using only ONE of the following tools:\n"
            "- nmap: for scanning ports, hosts, services\n"
            "- whois: for WHOIS lookup of domains\n"
            "- dig: for DNS record lookups\n\n"
            "⚠️ Rules:\n"
            "- Do NOT include explanations, markdown, or code blocks\n"
            "- Do NOT include unnecessary flags like `-d` unless it's required for that tool\n"
            "- For dnsenum, use the correct syntax: `dnsenum domain.com`\n"
            "- Never use sudo\n"
            "- Only return one valid command\n\n"
            f"{prompt}"
        ),
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    raw = response.json()["response"].strip()
    command = raw.splitlines()[0]
    command = re.sub(r"^`+|`+$", "", command)
    command = re.sub(r"^bash\s*", "", command, flags=re.IGNORECASE)
    return command.strip()
