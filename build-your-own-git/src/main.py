"""
Build Your Own Git – Minimal Version Control System
Author: Ihunna Amugo | Build-Your-Own-X Series

🧬 Goal:
Recreate basic Git features like:
- init
- add
- commit
- log

This mimics what happens under the hood of `git` — useful for managing simulation logs, digital twin versions, or model states in clinical AI workflows.
"""

import os
import hashlib
import json
import time
from pathlib import Path

# Create hidden directory for versioning
GIT_DIR = ".ihgit"
STAGE_FILE = os.path.join(GIT_DIR, "stage.json")
LOG_FILE = os.path.join(GIT_DIR, "log.json")

def init():
    os.makedirs(GIT_DIR, exist_ok=True)
    with open(STAGE_FILE, 'w') as f:
        json.dump({}, f)
    with open(LOG_FILE, 'w') as f:
        json.dump([], f)
    print("✅ Initialized empty ihgit repo.")

def add(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    file_hash = hashlib.sha1(content.encode()).hexdigest()
    with open(STAGE_FILE, 'r') as f:
        staged = json.load(f)
    staged[file_path] = {"hash": file_hash, "content": content}
    with open(STAGE_FILE, 'w') as f:
        json.dump(staged, f)
    print(f"📥 Staged {file_path}")

def commit(message):
    with open(STAGE_FILE, 'r') as f:
        staged = json.load(f)
    if not staged:
        print("⚠️ Nothing to commit.")
        return
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    commit_id = hashlib.sha1((message + timestamp).encode()).hexdigest()[:8]
    with open(LOG_FILE, 'r') as f:
        log = json.load(f)
    log.append({"id": commit_id, "msg": message, "time": timestamp, "files": staged})
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)
    with open(STAGE_FILE, 'w') as f:
        json.dump({}, f)
    print(f"✅ Committed: {commit_id} | {message}")

def log_history():
    with open(LOG_FILE, 'r') as f:
        log = json.load(f)
    for entry in reversed(log):
        print(f"🔸 {entry['id']} - {entry['msg']} ({entry['time']})")

# 🧪 Sample usage
if __name__ == "__main__":
    print("=== ihgit: Mini Git Clone ===")
    print("Commands: init, add <file>, commit <msg>, log")

    while True:
        command = input("ihgit > ").strip()
        if command == "exit":
            break
        elif command == "init":
            init()
        elif command.startswith("add "):
            _, file = command.split(maxsplit=1)
            add(file)
        elif command.startswith("commit "):
            _, msg = command.split(" ", 1)
            commit(msg)
        elif command == "log":
            log_history()
        else:
            print("Unknown command.")
