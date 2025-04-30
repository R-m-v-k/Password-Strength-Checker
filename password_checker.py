#!/usr/bin/env python3

import re
import argparse
from termcolor import colored

def check_password_strength(password):
    # Check different aspects of the password
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'[0-9]', password))
    special_char = bool(re.search(r'[^A-Za-z0-9]', password))

    # Calculate score
    score = sum([length, uppercase, lowercase, digit, special_char])

    # Return strength category
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

def main():
    parser = argparse.ArgumentParser(
        description="🔒 Password Strength Checker - Evaluate your password security!"
    )
    parser.add_argument(
        '-p', '--password',
        type=str,
        help='Password to check the strength for.'
    )
    args = parser.parse_args()

    if not args.password:
        print(colored("[!] Please provide a password with -p or --password.", "red"))
        return

    strength = check_password_strength(args.password)

    # Colored output
    if strength == "Strong":
        print(colored(f"Password Strength: {strength} 💪", "green"))
    elif strength == "Moderate":
        print(colored(f"Password Strength: {strength} ⚡", "yellow"))
    else:
        print(colored(f"Password Strength: {strength} ❌", "red"))

if __name__ == "__main__":
    main()
