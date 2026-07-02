"""
========================================================
  Password Strength Checker - Cybersecurity Tool
  Author  : Aastha Nitin Nandekar
  Tech    : Python 3
  Domain  : Cybersecurity / Cryptography Basics
========================================================

Features:
  - Checks password strength (Weak / Medium / Strong / Very Strong)
  - Detects missing security criteria
  - Estimates brute-force crack time
  - Suggests stronger passwords
  - Color-coded terminal output
  - Clean report generation
"""

import re
import math
import random
import string
import time


# ──────────────────────────────────────────────
#  ANSI Color Codes for Terminal Output
# ──────────────────────────────────────────────
class Color:
    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    GREEN   = "\033[92m"
    CYAN    = "\033[96m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"


# ──────────────────────────────────────────────
#  Password Strength Analyzer
# ──────────────────────────────────────────────
class PasswordStrengthChecker:

    def __init__(self, password: str):
        self.password = password
        self.length   = len(password)
        self.score    = 0
        self.feedback = []
        self.checks   = {}

    def analyze(self) -> dict:
        """Run all checks and return a full analysis report."""
        self._check_length()
        self._check_uppercase()
        self._check_lowercase()
        self._check_digits()
        self._check_special_characters()
        self._check_common_patterns()
        self._calculate_score()
        return self._build_report()

    # ── Individual Checks ──────────────────────

    def _check_length(self):
        if self.length >= 16:
            self.score += 3
            self.checks["Length (16+)"] = True
        elif self.length >= 12:
            self.score += 2
            self.checks["Length (12+)"] = True
        elif self.length >= 8:
            self.score += 1
            self.checks["Length (8+)"] = True
        else:
            self.checks["Length (8+)"] = False
            self.feedback.append("Use at least 8 characters (12+ recommended).")

    def _check_uppercase(self):
        has = bool(re.search(r"[A-Z]", self.password))
        self.checks["Uppercase Letter"] = has
        if has:
            self.score += 1
        else:
            self.feedback.append("Add at least one uppercase letter (A–Z).")

    def _check_lowercase(self):
        has = bool(re.search(r"[a-z]", self.password))
        self.checks["Lowercase Letter"] = has
        if has:
            self.score += 1
        else:
            self.feedback.append("Add at least one lowercase letter (a–z).")

    def _check_digits(self):
        has = bool(re.search(r"\d", self.password))
        self.checks["Number (0–9)"] = has
        if has:
            self.score += 1
        else:
            self.feedback.append("Include at least one number (0–9).")

    def _check_special_characters(self):
        has = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\;'/`~]", self.password))
        self.checks["Special Character (!@#...)"] = has
        if has:
            self.score += 2
        else:
            self.feedback.append("Add special characters like !@#$%^&*.")

    def _check_common_patterns(self):
        common = [
            "password", "123456", "qwerty", "abc123",
            "letmein", "welcome", "admin", "login",
            "iloveyou", "monkey", "dragon"
        ]
        lower_pwd = self.password.lower()
        is_common = any(word in lower_pwd for word in common)
        self.checks["No Common Patterns"] = not is_common
        if is_common:
            self.score -= 3
            self.feedback.append("Avoid common words like 'password', 'admin', '123456'.")

    # ── Score → Strength Label ─────────────────

    def _calculate_score(self):
        self.score = max(0, self.score)  # no negative score

    def _get_strength(self) -> tuple:
        if self.score >= 8:
            return "Very Strong", Color.GREEN
        elif self.score >= 6:
            return "Strong", Color.CYAN
        elif self.score >= 4:
            return "Medium", Color.YELLOW
        else:
            return "Weak", Color.RED

    # ── Crack Time Estimator ───────────────────

    def _estimate_crack_time(self) -> str:
        """Estimate brute-force crack time at 1 billion guesses/second."""
        charset_size = 0
        if re.search(r"[a-z]", self.password): charset_size += 26
        if re.search(r"[A-Z]", self.password): charset_size += 26
        if re.search(r"\d",    self.password): charset_size += 10
        if re.search(r"[^a-zA-Z0-9]", self.password): charset_size += 32
        if charset_size == 0: charset_size = 26

        combinations = charset_size ** self.length
        seconds = combinations / 1_000_000_000  # 1 billion guesses/sec

        if seconds < 1:
            return "Instantly"
        elif seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.1f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.1f} hours"
        elif seconds < 31536000:
            return f"{seconds/86400:.1f} days"
        elif seconds < 3153600000:
            return f"{seconds/31536000:.1f} years"
        else:
            return f"{seconds/31536000:.2e} years (practically uncrackable)"

    # ── Password Suggestion ────────────────────

    def _suggest_password(self) -> str:
        """Generate a strong random password suggestion."""
        chars = (
            random.choices(string.ascii_uppercase, k=3) +
            random.choices(string.ascii_lowercase, k=4) +
            random.choices(string.digits, k=3)          +
            random.choices("!@#$%^&*", k=2)
        )
        random.shuffle(chars)
        return "".join(chars)

    # ── Build Final Report ─────────────────────

    def _build_report(self) -> dict:
        strength, color = self._get_strength()
        return {
            "password"    : self.password,
            "length"      : self.length,
            "score"       : self.score,
            "strength"    : strength,
            "color"       : color,
            "checks"      : self.checks,
            "feedback"    : self.feedback,
            "crack_time"  : self._estimate_crack_time(),
            "suggestion"  : self._suggest_password(),
        }


# ──────────────────────────────────────────────
#  Display Report in Terminal
# ──────────────────────────────────────────────
def display_report(report: dict):
    c = Color
    print("\n" + "=" * 52)
    print(f"{c.BOLD}         🔐 PASSWORD STRENGTH REPORT{c.RESET}")
    print("=" * 52)

    print(f"\n  {'Password':<22}: {c.BOLD}{report['password']}{c.RESET}")
    print(f"  {'Length':<22}: {report['length']} characters")

    strength_colored = f"{report['color']}{c.BOLD}{report['strength']}{c.RESET}"
    print(f"  {'Strength':<22}: {strength_colored}")
    print(f"  {'Score':<22}: {report['score']} / 8")
    print(f"  {'Crack Time Estimate':<22}: {report['crack_time']}")

    print(f"\n{c.BOLD}  Security Checklist:{c.RESET}")
    for check, passed in report["checks"].items():
        icon = f"{c.GREEN}✔{c.RESET}" if passed else f"{c.RED}✘{c.RESET}"
        print(f"    {icon}  {check}")

    if report["feedback"]:
        print(f"\n{c.BOLD}  💡 Suggestions to Improve:{c.RESET}")
        for tip in report["feedback"]:
            print(f"    {c.YELLOW}→{c.RESET}  {tip}")

    print(f"\n{c.BOLD}  🔑 Suggested Strong Password:{c.RESET}")
    print(f"    {c.CYAN}{report['suggestion']}{c.RESET}")

    print("\n" + "=" * 52 + "\n")


# ──────────────────────────────────────────────
#  Main Program
# ──────────────────────────────────────────────
def main():
    print(f"\n{'='*52}")
    print(f"  🔐  Password Strength Checker  |  Cybersecurity")
    print(f"  {'Author: Aastha Nitin Nandekar':^48}")
    print(f"{'='*52}")
    print("  Type 'quit' to exit anytime.\n")

    while True:
        password = input("  Enter password to check: ").strip()

        if password.lower() == "quit":
            print("\n  Exiting. Stay secure! 🔒\n")
            break

        if not password:
            print("  ⚠  Password cannot be empty. Try again.\n")
            continue

        checker = PasswordStrengthChecker(password)
        report  = checker.analyze()
        display_report(report)

        again = input("  Check another password? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Exiting. Stay secure! 🔒\n")
            break
        print()


if __name__ == "__main__":
    main()