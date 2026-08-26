# 🔐 Password Strength Checker

A **Python-based cybersecurity tool** that analyzes the strength of any password and gives detailed feedback, crack time estimation, and a stronger password suggestion — all in a clean, color-coded terminal interface.

---

# 🚀 Live Demo

```
====================================================
         🔐 PASSWORD STRENGTH REPORT
====================================================

  Password              : MyP@ssw0rd!
  Length                : 11 characters
  Strength              : Strong
  Score                 : 7 / 8
  Crack Time Estimate   : 3.45e+14 years (practically uncrackable)

  Security Checklist:
    ✔  Length (8+)
    ✔  Uppercase Letter
    ✔  Lowercase Letter
    ✔  Number (0–9)
    ✔  Special Character (!@#...)
    ✔  No Common Patterns

  💡 Suggestions to Improve:
    →  Use at least 12+ characters for maximum security.

  🔑 Suggested Strong Password:
    Kx3@mLp!9Qr
====================================================
```

---

#✨ Features

- ✅ Strength rating — **Weak / Medium / Strong / Very Strong**
- ✅ Weighted scoring system (score out of 8)
- ✅ Security checklist with pass/fail for each criterion
- ✅ **Brute-force crack time estimator** (at 1 billion guesses/sec)
- ✅ Actionable feedback to improve your password
- ✅ Auto-generates a strong password suggestion
- ✅ Color-coded terminal output using ANSI codes
- ✅ Loop-based CLI — check multiple passwords in one session
- ✅ No external libraries — pure Python 3

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

**Concepts used:**
- Object Oriented Programming (OOP)
- Regular Expressions (`re` module)
- String manipulation
- Math & entropy calculation
- ANSI terminal formatting

---

## 📁 Project Structure

```
password-strength-checker/
└── password_strength_checker.py   # Main program
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/aasthanandekar/password-strength-checker.git
cd password-strength-checker
```

**2. Run the program**
```bash
python password_strength_checker.py
```

> ✅ No installations needed — uses Python standard library only.

---

## 🧠 How It Works

| Check | Points |
|---|---|
| Length 8+ | +1 |
| Length 12+ | +2 |
| Length 16+ | +3 |
| Uppercase letter | +1 |
| Lowercase letter | +1 |
| Number (0–9) | +1 |
| Special character | +2 |
| Common pattern detected | −3 |

**Strength Levels:**

| Score | Strength |
|---|---|
| 0 – 3 | 🔴 Weak |
| 4 – 5 | 🟡 Medium |
| 6 – 7 | 🔵 Strong |
| 8+ | 🟢 Very Strong |

---

## 💼 Resume Description

> **Password Strength Checker** | Python, Regex, OOP
> Built a CLI-based cybersecurity tool that analyzes password strength using pattern matching and a weighted scoring algorithm. Features include brute-force crack time estimation, a security checklist, and auto-suggestion of strong passwords.

---

## 👩‍💻 Author

**Aastha Nitin Nandekar**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/AasthaNandekar)
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/aasthanandekar)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:eraasthanandekar@gmail.com)

---


