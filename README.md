#  NetraSuite  
**LLM-Powered Network Security Assistant Tool**

<img width="628" alt="banner" src="https://github.com/user-attachments/assets/782251bb-8caa-440a-8235-60b68e781d01" />

NetraSuite is a terminal-based AI assistant that converts natural language prompts into real network reconnaissance commands using tools like `nmap`, `whois`, and `dig`. It uses a local LLM served via [Ollama](https://ollama.com), and provides clean, interpretable command execution — all through a conversational terminal interface.

---

## 📦 Features

- Translate natural language into actual Linux commands
- Auto-selects the best-suited tool for each query
- Domain name resolution for tools that require IPs
- Clear, readable terminal output using `rich`
- Built-in setup script to install everything
- No internet dependency — runs fully offline via Ollama

---

## 🛠️ Requirements

### ✅ Python 3.8+

Install Python dependencies:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
rich>=13.0.0
requests>=2.25.0
pyfiglet>=0.8
readline; sys_platform == "linux"
```

---

## 🔧 Setup

Run the post-install setup:

```bash
python3 post_install.py
```

This will:
- Install required tools: `nmap`, `whois`, `dig`
- Install & launch [Ollama](https://ollama.com)
- Pull the `mistral` model
- Verify everything is ready to go

---

## 🚀 Usage

Start NetraSuite:

```bash
python3 -m netrasuite
```

You’ll see the banner and a prompt:

```
netrasuite >
```

Now, simply type what you want it to do 👇

---

## 💬 Example Prompts

| Prompt                                                   | Tool Used |
|-----------------------------------------------------------|-----------|
| scan localhost for open ports                             | `nmap`    |
| scan the domain tesla.com from port 20 to 443             | `nmap`    |
| perform whois lookup on google.com                        | `whois`   |
| who owns the domain openai.com                            | `whois`   |
| get A record of github.com                                | `dig`     |
| fetch MX and TXT records for protonmail.com               | `dig`     |

---

## 🧠 Built-in Commands

| Command          | Description                          |
|------------------|--------------------------------------|
| `help`           | Show help and example prompts        |
| `clear`          | Clear the screen                     |
| `restart`        | Restart the assistant                |
| `about`          | Show tool version and creator        |
| `exit` / `quit`  | Exit the tool                        |
| `/bye`           | Exit the tool and clean Ollama cache |

## 📁 Output Preview

```bash
Interpreted Command: nmap -A 192.168.1.1

Nmap Summary:
Target: 192.168.1.1
Host Status: Up (0.003s latency)
Open Ports:
╭────┬───────┬────────┬────────────────────╮
│ 22 │ open  │ ssh    │ OpenSSH 8.2p1      │
│ 80 │ open  │ http   │ Apache httpd 2.4.41│
╰────┴───────┴────────┴────────────────────╯
