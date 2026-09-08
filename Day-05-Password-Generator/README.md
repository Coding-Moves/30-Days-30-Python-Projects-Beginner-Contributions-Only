# Day 05: Password Generator

A secure and customizable command-line password generator built with Python's built-in `secrets` and `string` modules.

## Features

- Cryptographically secure random generation using `secrets.SystemRandom`
- Customizable password length (default: 16 characters)
- Configurable character sets:
  - Uppercase letters (`A-Z`)
  - Lowercase letters (`a-z`)
  - Digits (`0-9`)
  - Special punctuation symbols
- Guarantees at least one character from each selected character category
- Pure standard library implementation with zero external dependencies

## How to Run

Run the script using Python 3:

```bash
python main.py
```

## Sample Output

```text
=== Password Generator ===
Generate secure, random passwords with customizable options.

Enter password length (minimum 4, default 16): 14
Include uppercase letters (A-Z)? [Y/n]: y
Include numbers (0-9)? [Y/n]: y
Include symbols (@#$%...)? [Y/n]: y

Generated Password:
------------------
k9#Vp2$mQ8!zX1
------------------
Length: 14 characters
```
