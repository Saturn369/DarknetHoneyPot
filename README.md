# DarknetHoneyPot
A literal darknet honeypot. Use it for inspiration or for your cybersecurity portfolio.

---

## Overview

This project is a **darknet honeypot** built using Flask. It is designed to simulate a fake credit card marketplace to attract malicious actors. The purpose is to monitor and study behavior without hosting or interacting with any real card data. Ideal for educational and research applications in cybersecurity.

---

## 🚨 Disclaimer

This honeypot is for **educational and research purposes only**. It must be run in a secure, isolated environment and should never be used to engage, entrap, or deceive real individuals.

**No real card data is involved or encouraged.**

---

## 🔧 Features

- Simulated credit card (BIN) listings.
- Fake login and fake purchase endpoints (log-only).
- Logs all interaction attempts (routes accessed, IP, timestamps).
- Designed for deployment as a `.onion` site on the Tor network.
- Simple, easy-to-edit front-end using Jinja2 with `index.html`.

---

## 📁 Project Structure

```
DarknetHoneyPot/
├── honeypot.py           # Main Flask application
└── templates/
    └── index.html        # Fake storefront HTML page
```

---

## 🚀 Getting Started

### 1. Install Flask

```bash
pip install flask
```

### 2. Run the Flask App

```bash
python honeypot.py
```

Ensure your app is set to:

```python
app.run(host="127.0.0.1", port=5000)
```

### 3. Configure Tor Hidden Service

Edit your `torrc` file to include the following:

```
HiddenServiceDir C:\path\to\TorDocs
HiddenServicePort 80 127.0.0.1:5000
```

Restart Tor. Your `.onion` address will be available inside the `hostname` file located in `TorDocs`.

---

## 📜 Logging

All attempted interactions (login or purchase) are logged to:

```
honeypot_log.txt
```

Each log entry includes:
- Timestamp
- IP address (via Tor)
- Endpoint accessed

---

## 📘 Use Cases

- Build a personal cybersecurity project portfolio.
- Learn about darknet hosting and Tor configurations.
- Study honeypot behavior for red team/blue team exercises.

---

## 🛑 Reminder

**Never use this project to communicate with or mislead real users.**
**Do not collect, store, or post actual personal information.**

Use this project responsibly and legally.

