# 🧬 Build Your Own Git (Mini Version Control System)

This project recreates the basic versioning features of Git using only Python. It helps explain how `git init`, `add`, `commit`, and `log` actually work — essential for research workflows, model tracking, or regulatory AI systems.

---

## 📌 Features

- `init`: Creates a `.ihgit/` directory to hold commits
- `add <file>`: Reads file contents and stores its hash
- `commit "msg"`: Saves current stage with a timestamp and message
- `log`: Shows commit history with file details

---

## 🧠 Why It Matters in Healthcare AI

Many health AI systems need to:
- Track model updates
- Store simulation input/output versions
- Keep an auditable history of predictions

This project gives you a sense of:
- How model registries work
- How digital twins can checkpoint state
- How EHR snapshots could be versioned safely

---

## 🚀 Usage

```bash
cd src/
python main.py
```

Then try:
```
init
add notes.txt
commit "first version"
log
exit
```

---

## 🗂️ Structure

- `src/main.py` – All version control logic
- `.ihgit/` – Auto-created to store commits
- `assets/` – Optional screenshots or diffs
- `NOTES.md` – Space to jot learning insights

---

## 👩🏾‍⚕️ Author

**Ihunna Amugo**  
DDS Candidate | MHA | MS | REHS | PhD(c) Computational Engineering  
GitHub: [@ihunnamatata](https://github.com/ihunnamatata)
