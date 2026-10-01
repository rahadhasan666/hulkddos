# 🛡️ HulkDDoS

### Authorized HTTP Load & Stress Testing Toolkit

HulkDDoS is a security research and HTTP load-testing project intended for **authorized testing environments**. It can be used to study application behavior, server performance, network handling, and defensive security mechanisms.

> ⚠️ **Legal & Ethical Use Only**
>
> Use this project only against systems that you own or have explicit authorization to test. Do not use it to disrupt, overload, or attack third-party infrastructure.

---

## ✨ Features

* 🌐 HTTP/HTTPS testing
* 📊 Controlled traffic testing
* 🔬 Security research
* 🧪 Application stress testing
* 🐍 Python support
* 🟢 Node.js support
* 📱 Termux compatibility
* 🐧 Debian-based Linux compatibility
* 🔧 Virtual-environment based Python installation

---

## 🖥️ Supported Environments

* Kali Linux
* Debian
* Ubuntu
* Termux
* Other compatible Linux environments

---

# 🐧 Kali / Debian / Ubuntu

## 1. Install System Dependencies

```bash
sudo apt update

sudo apt install -y \
git \
golang \
perl \
python3 \
python3-full \
python3-venv \
python3-pip \
nodejs \
npm
```

---

## 2. Clone Repository

```bash
git clone https://github.com/rahadhasan666/hulkddos.git
cd hulkddos
```

---

## 3. Create Python Virtual Environment

Modern Kali/Debian systems use **PEP 668**, which can prevent system-wide `pip` installations.

Create an isolated virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Your terminal should now show something similar to:

```text
(.venv) root@kali:~/hulkddos#
```

---

## 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 5. Install Python Dependencies

```bash
python -m pip install -r requirements.txt
```

This avoids the:

```text
error: externally-managed-environment
```

error without modifying the system Python installation.

---

## 🔄 Activate Environment Again

Whenever you open a new terminal:

```bash
cd ~/hulkddos
source .venv/bin/activate
```

To leave the virtual environment:

```bash
deactivate
```

---

# 📱 Termux Installation

## 1. Update Termux

```bash
pkg update && pkg upgrade -y
```

---

## 2. Install Required Packages

```bash
pkg install -y git python nodejs
```

---

## 3. Clone Repository

```bash
git clone https://github.com/rahadhasan666/hulkddos.git
cd hulkddos
```

---

## 4. Create Python Virtual Environment

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## 5. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 6. Install Python Requirements

```bash
python -m pip install -r requirements.txt
```

---

## 🔄 Reactivate the Environment

After reopening Termux:

```bash
cd ~/hulkddos
source .venv/bin/activate
```

---

# 📦 Node.js Dependencies

Install the dependencies declared by the project:

```bash
npm install
```

If you are developing or modifying the project, use the `package.json` file as the source of truth for Node.js dependencies.

---

# 🧪 Authorized Testing

Use the project only in environments where you have permission to perform testing.

Recommended development targets:

```text
localhost
127.0.0.1
Private test servers
Development environments
Authorized staging infrastructure
```

A typical authorized workflow:

```text
┌──────────────────────┐
│ Development Server   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Controlled Test      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Monitor Resources    │
│ CPU / RAM / Network  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Analyze Results      │
└──────────────────────┘
```

---

# 📊 System Monitoring

During authorized testing, monitor the test server.

### CPU / Memory

```bash
top
```

or:

```bash
htop
```

### Network Connections

```bash
ss -s
```

---

# 🛡️ Defensive Security

When evaluating your own infrastructure, consider implementing:

* Rate limiting
* Request throttling
* Connection limits
* Reverse proxies
* Web Application Firewalls
* CDN protection
* IP reputation filtering
* Application monitoring
* Server logging
* Automated alerting

---

# 📁 Project Structure

```text
hulkddos/
│
├── hk.py
├── requirements.txt
├── package.json
├── package-lock.json
├── .venv/
└── README.md
```

---

# 🔧 Development Setup

Clone the repository:

```bash
git clone https://github.com/rahadhasan666/hulkddos.git
cd hulkddos
```

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
npm install
```

---

# 🚫 Avoid System-Wide pip Installation

Do **not** use:

```bash
sudo pip3 install -r requirements.txt
```

on modern Kali/Debian systems.

Do not use:

```bash
pip3 install --break-system-packages
```

unless you specifically understand the consequences.

The recommended approach is:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

---

# ⚠️ Important Disclaimer

This project is provided for:

* Education
* Security research
* Authorized load testing
* Development
* Defensive security testing

Do **not** use this project to:

* Attack websites
* Perform unauthorized DDoS attacks
* Disrupt third-party services
* Overload infrastructure without permission
* Circumvent security protections
* Bypass CAPTCHA or anti-bot systems
* Hide malicious traffic

The user is solely responsible for ensuring that their use of this software complies with applicable laws, policies, and authorization requirements.

---

# 👨‍💻 Developer

**Rahad Hasan**

GitHub:

`https://github.com/rahadhasan666`

Repository:

`https://github.com/rahadhasan666/hulkddos`

---

# 📜 License

This project is intended for educational and authorized security-testing purposes.

See the repository's license file for applicable licensing terms.

---

## ⭐ Support

If you find this project useful for legitimate security research or development, consider giving the repository a ⭐ on GitHub.

**Use responsibly. Test only with permission.**
