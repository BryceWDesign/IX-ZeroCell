# 🔐 Security Policy

## 📅 Supported Versions

**IX-ZeroCell** is currently in `v1.0-alpha`. During this phase:

- All critical hardware and firmware vulnerabilities will be prioritized and patched.
- Contributions involving attack vectors, data leaks, or unsafe power conditions are treated as high priority.

| Version       | Supported |
|---------------|-----------|
| `v1.0-alpha`  | ✅ Yes     |
| Pre-release   | ❌ No      |
| Forked builds | ❌ No (report upstream)

---

## 📣 Reporting a Vulnerability

If you discover a vulnerability in **IX-ZeroCell**, especially one involving:

- Safety hazards (electrical shorts, thermal runaway, etc.)
- Power storage overcharge/undervoltage behaviors
- Firmware logic that may lead to failure or physical harm
- RF harvesting misbehavior or unintended emissions

Please report it **privately**

Include:

- A clear description of the issue
- Steps to reproduce or affected hardware segment
- Whether it's confirmed, suspected, or theoretical
- Your preferred name (or anonymous handle)

---

## 🤝 What Happens Next?

1. We will acknowledge receipt within **3 business days**
2. We’ll review and reproduce the issue (if applicable)
3. You’ll receive a timeline and status update on remediation
4. Fixes will be pushed under a security-tagged release
5. You may optionally be credited in `ACKNOWLEDGEMENTS.md`

---

## 🧰 Scope of Coverage

We accept reports related to:

- Hardware design flaws (EMF risks, shorts, weak traces)
- Firmware exploits or unsafe states
- Environmental risks from poor harvesting behaviors
- Any circuit, logic, or assembly component directly from this repo

We **do not** cover:

- Physical misuse (e.g. submerged without protection)
- User wiring errors
- Third-party fork variants

---

## 🧪 Bonus: Experimental Modules

Experimental modules (e.g., RF harvesting extensions, wireless charging forks) are marked clearly in `README.md`. Vulnerabilities there are accepted but prioritized lower unless safety-critical.

---

## 🛡️ Our Pledge

We’re committed to building **safe**, **open**, and **responsibly engineered** technology.  
We appreciate every ethical disclosure — and we’ll treat every report with respect and urgency.

— The **IX-ZeroCell** Maintainer Team  


