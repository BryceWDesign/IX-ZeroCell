# Contributing to IX-ZeroCell

🚀 Thank you for your interest in contributing to **IX-ZeroCell** — a fully open-source, battery-free hybrid energy system. Whether you're fixing typos, improving firmware, refining hardware, or sharing field testing data — all contributions are welcome.

---

## 📐 Contribution Types

You can contribute in many ways:

- 🛠️ **Hardware**: Design improvements, part substitutions, alternate coil winding specs
- 💻 **Firmware**: Code improvements, bug fixes, feature additions
- 📄 **Documentation**: Fix typos, add clarity, contribute translations
- 🔬 **Testing & Feedback**: Submit results from field use, shake tests, environmental analysis
- 📷 **Photos/Videos**: Share builds or deployments of IX-ZeroCell in action

---

## 🧰 How to Contribute

### 1. Fork the Repository
Use the GitHub "Fork" button at the top of the repo page to create your own copy.

### 2. Create a Feature Branch
Name it clearly:
```bash
git checkout -b fix/supercap-charging-bug
```

### 3. Make Your Changes
Follow the repo's formatting rules. Keep commits focused — one file or fix at a time.

### 4. Commit Your Work
Use **clear and descriptive commit messages**:
```bash
git commit -m "Fix: resolved boost converter voltage drift under load"
```

### 5. Push and Open a Pull Request
```bash
git push origin fix/supercap-charging-bug
```

Then visit your fork on GitHub and open a Pull Request (PR). The team will review, test, and merge if accepted.

---

## 🧼 Style Guidelines

- Use `snake_case` for file names and `camelCase` for variables (firmware).
- Keep documentation in **Markdown** and use existing templates.
- Match existing file headers and author block where possible.
- All changes must retain compatibility with batteryless architecture.

---

## 📢 Before You Start

Please check for existing:
- **[Issues](../../issues)** — your bug/feature may already be tracked.
- **[Pull Requests](../../pulls)** — someone may be working on a fix.

If in doubt, [open an Issue](../../issues/new) before beginning a major change.

---

## 👤 Contributor Credit

All merged contributors will be listed in the `ACKNOWLEDGEMENTS.md` file (coming soon). We don’t use pen names unless explicitly requested.

---

## 🛡️ Licensing

All contributions to this project fall under the [Apache License 2.0](./LICENSE)
By submitting code, hardware, or docs, you agree your work will be published under the same license.

---

Thanks again for helping shape the future of batteryless tech.
— **Bryce Wooster**
Creator, IX-ZeroCell

# Current contribution requirements

Read the current README, `docs/RESEARCH_AND_DECISIONS.md` and `docs/BENCH_VALIDATION.md`. Run `python scripts/verify.py` for code changes. Model inputs must be labeled as assumptions; measured claims require raw instrument evidence and independent review. Do not restore the withdrawn historical output/compliance claims or report a passing simulation as physical power generation.

The older contribution text below is retained as project history where applicable.
