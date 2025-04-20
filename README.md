# 👁️ NetraSuite

**NetraSuite** is a terminal-based, LLM-powered network security assistant that lets you run tools like `nmap`, `tshark`, `zeek`, and `nfdump` using simple natural language prompts.

---

## 🚀 Features

- 🔍 Run `nmap` scans via prompts like `"scan IP 192.168.1.1 for open ports"`
- 🧠 Use local LLMs (via [Ollama](https://ollama.com)) to interpret your intent
- 🖥️ Live packet capture with `tshark`
- 📄 Analyze PCAP files with `zeek`
- 📊 Visualize NetFlow data with `nfdump`
- 🌈 Beautiful CLI output using [`rich`](https://github.com/Textualize/rich)

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/youruser/netrasuite.git
cd netrasuite
```

### 2. Install Python Requirements
```bash
pip install -r requirements.txt
```

### 3. Run Post-Install Script (auto installs system tools + ollama)
```bash
python post_install.py
```

---

## 🧠 Usage

### Start the CLI
```bash
python -m netrasuite
```

### Example Prompts
```bash
netrasuite > scan network 192.168.1.1 for open ports and services
netrasuite > capture network traffic on interface eth0
netrasuite > analyze pcap file capture.pcap with zeek
netrasuite > show top talkers from netflow data
```

---

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
```

---

## 🔧 Tools Required

- [`nmap`](https://nmap.org)
- [`tshark`](https://www.wireshark.org)
- [`zeek`](https://zeek.org)
- [`nfdump`](https://github.com/phaag/nfdump)
- [`ollama`](https://ollama.com) + `mistral` model

---

## ✨ Roadmap

- [ ] Add export to JSON / Markdown
- [ ] Add interactive mode
- [ ] Add support for other security tools
- [ ] Multi-language CLI support (Nepali 🇳🇵 / English)

---

## 📜 License

MIT License---

## 🧪 How to Run NetraSuite

Follow these steps to get started with NetraSuite:

---

### 🛠️ Prerequisites

Make sure your system has the following installed:

- Python 3.8 or higher
- Git
- Internet access for installing packages
- sudo privileges (for installing system tools like `nmap`, `zeek`, etc.)

---

### 🚀 1. Clone the Project

```bash
git clone https://github.com/youruser/netrasuite.git
cd netrasuite
```

Or if you've downloaded the ZIP:

```bash
unzip netrasuite_project.zip
cd netrasuite_project
```

---

### 📦 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 🧰 3. Run Environment Setup

This installs required tools: `nmap`, `tshark`, `zeek`, `nfdump`, and `ollama`.  
It also pulls the `mistral` model for prompt interpretation.

```bash
python post_install.py
```

---

### 💻 4. Start NetraSuite

Run the tool via:

```bash
python -m netrasuite
```

You’ll enter an interactive CLI like:

```bash
👁️  NetraSuite — LLM-Powered Network Assistant
netrasuite >
```

---

### 🧠 5. Try Natural Language Prompts

Example prompts:

```bash
netrasuite > scan IP 192.168.1.1 for open ports
netrasuite > capture traffic on interface eth0
netrasuite > analyze pcap file with zeek
netrasuite > show top talkers from netflow logs
```

---

### 🌍 (Optional) Install as a Global CLI

To run NetraSuite from anywhere in your terminal:

```bash
pip install .
```

Now you can just run:

```bash
netrasuite "scan 192.168.1.1 for ports"
```

---

### ✅ Output Preview

```bash
Interpreted Command: nmap -A 192.168.1.1

Target: 192.168.1.1
Host Status: Up (0.003s latency)
Open Ports:
╭────┬───────┬────────┬────────────────────╮
│ 22 │ open  │ ssh    │ OpenSSH 8.2p1      │
│ 80 │ open  │ http   │ Apache httpd 2.4.41│
╰────┴───────┴────────┴────────────────────╯
```

---

You're now ready to use NetraSuite to simplify and power-up your network investigations! 🎯