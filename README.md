# Password Strength Checker

A simple **command-line Password Strength Checker** written in Python. This tool helps evaluate the strength of a given password based on common security criteria.

## Features

- **Length Check**: Ensures the password is at least 8 characters long.
- **Character Diversity**: Checks for the presence of:
  - Uppercase letters (`A-Z`)
  - Lowercase letters (`a-z`)
  - Digits (`0-9`)
  - Special characters (e.g., `@`, `#`, `$`, etc.)

## Strength Scoring

The tool evaluates password strength using the following scale:

- **Strong**: All five conditions met.
- **Moderate**: At least three out of five conditions met.
- **Weak**: Fewer than three conditions met.

## Usage

Run the script from the command line:

```bash
python3 password_checker.py -p "YourPasswordHere"
