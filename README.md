🛡️ Windows Registry Change Monitoring System
📌 Project Overview

The Windows Registry Change Monitoring System is a defensive security project designed to detect, log, and alert on unauthorized or suspicious changes made to critical Windows registry keys.

The Windows Registry stores essential configuration data related to system startup, security policies, and application behavior. Malware often abuses these registry locations to maintain persistence, disable security tools, or modify system behavior.

This project helps identify such activities through baseline comparison and continuous monitoring.

🎯 Project Objectives

Monitor autorun registry keys used for startup persistence

Detect malware-like registry modifications

Create a baseline snapshot for registry integrity checking

Log and alert on additions, deletions, and modifications

Generate an audit trail for security analysis and forensics

🧠 Why This Project Is Important

Registry changes are a common malware persistence technique

Unauthorized registry edits can indicate:

Malware infection

Privilege misuse

Security policy tampering

Manual registry inspection is impractical and error-prone

This project provides hands-on Blue Team experience used in:

SOC monitoring

Incident response

Digital forensics

⚙️ How the Project Works
1️⃣ Sensitive Key Selection

The system monitors high-risk registry paths such as:

HKCU\...\Run

HKLM\...\Run

Windows Defender policy keys

2️⃣ Baseline Creation

On the first run, the program captures the current registry state

Saves it as baseline.json

This baseline represents a trusted clean state

3️⃣ Continuous Monitoring

The script runs continuously

At regular intervals, it:

Reads current registry values

Compares them with the baseline

4️⃣ Change Detection

The system detects:

✅ New registry values added

⚠ Modified existing values

❌ Deleted values

5️⃣ Alerting & Logging

Detected changes are:

Displayed in the terminal

Logged into registry_changes.log

Logs include timestamp and change type

📂 Project Structure
registry_monitor/
├── main.py                 # Main monitoring script
├── baseline.json           # Registry baseline snapshot (auto-created)
├── registry_changes.log    # Change log file (auto-created)
└── README.md

🧪 How to Run the Project
Prerequisites

Windows OS

Python 3.x installed

Run terminal as Administrator

▶ Run the Script
python main.py


On first execution:

baseline.json is automatically created

Monitoring starts immediately

🧪 Testing the System
Test 1: Add Startup Entry

Open Registry Editor

Navigate to:

HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run


Add a new String Value

Observe alert in terminal and log file

Test 2: Delete Startup Entry

Delete the test value from the same registry path

The system logs the deletion event

📄 Sample Log Output
[2026-01-30 22:40:10] Registry Monitoring Started.
[2026-01-30 22:42:01] [ALERT] New registry value added in HKCU_Run: TestStartup
[2026-01-30 22:43:15] [WARNING] Registry value deleted from HKCU_Run: TestStartup

🔐 Security Note

⚠ This project:

Does NOT modify registry values

Performs read-only monitoring

Is intended for educational and defensive security purposes only

🎓 Learning Outcomes

Understanding Windows Registry structure

Identifying malware persistence techniques

Registry integrity monitoring

Python scripting for system security

Log analysis and incident detection

🧑‍💻 Author

Swapnil Govind Pathak

📜 License

This project is created for educational and academic use only.
