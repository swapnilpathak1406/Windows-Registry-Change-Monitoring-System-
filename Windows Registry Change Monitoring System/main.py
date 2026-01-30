import winreg
import json
import time
import os
from datetime import datetime

BASELINE_FILE = "baseline.json"
LOG_FILE = "registry_changes.log"
SCAN_INTERVAL = 10  # seconds

# Registry paths to monitor
MONITOR_KEYS = {
    "HKCU_Run": (winreg.HKEY_CURRENT_USER,
                 r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "HKLM_Run": (winreg.HKEY_LOCAL_MACHINE,
                 r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "Defender_Disable": (winreg.HKEY_LOCAL_MACHINE,
                         r"SOFTWARE\Policies\Microsoft\Windows Defender")
}


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")


def read_registry(key_root, subkey):
    data = {}
    try:
        with winreg.OpenKey(key_root, subkey) as key:
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(key, i)
                    data[name] = value
                    i += 1
                except OSError:
                    break
    except FileNotFoundError:
        pass
    return data


def create_baseline():
    baseline = {}
    for name, (root, path) in MONITOR_KEYS.items():
        baseline[name] = read_registry(root, path)

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    log_event("Baseline registry snapshot created.")


def load_baseline():
    if not os.path.exists(BASELINE_FILE):
        create_baseline()

    with open(BASELINE_FILE, "r") as f:
        return json.load(f)


def compare_registry(baseline):
    for name, (root, path) in MONITOR_KEYS.items():
        current = read_registry(root, path)
        old = baseline.get(name, {})

        # Detect added or modified values
        for key in current:
            if key not in old:
                log_event(f"[ALERT] New registry value added in {name}: {key} = {current[key]}")
            elif current[key] != old[key]:
                log_event(f"[WARNING] Registry value modified in {name}: {key}")

        # Detect deleted values
        for key in old:
            if key not in current:
                log_event(f"[WARNING] Registry value deleted from {name}: {key}")


def main():
    log_event("Registry Monitoring Started.")
    baseline = load_baseline()

    while True:
        compare_registry(baseline)
        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    main()
