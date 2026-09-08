import secrets
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    characters = list(string.ascii_lowercase)
    required = [secrets.choice(string.ascii_lowercase)]

    if use_uppercase:
        characters.extend(string.ascii_uppercase)
        required.append(secrets.choice(string.ascii_uppercase))

    if use_digits:
        characters.extend(string.digits)
        required.append(secrets.choice(string.digits))

    if use_special:
        characters.extend(string.punctuation)
        required.append(secrets.choice(string.punctuation))

    if length < len(required):
        raise ValueError(f"Length must be at least {len(required)} to satisfy selected character categories.")

    remaining = [secrets.choice(characters) for _ in range(length - len(required))]
    password_list = required + remaining

    system_random = secrets.SystemRandom()
    system_random.shuffle(password_list)

    return "".join(password_list)

def get_yes_no(prompt, default=True):
    choice = input(prompt).strip().lower()
    if not choice:
        return default
    return choice in ("y", "yes", "true", "1")

def main():
    print("=== Password Generator ===")
    print("Generate secure, random passwords with customizable options.\n")

    try:
        length_input = input("Enter password length (minimum 4, default 16): ").strip()
        length = int(length_input) if length_input else 16
        if length < 4:
            print("Length must be at least 4. Defaulting to 16.")
            length = 16
    except ValueError:
        print("Invalid number. Defaulting to 16.")
        length = 16

    use_upper = get_yes_no("Include uppercase letters (A-Z)? [Y/n]: ", True)
    use_digits = get_yes_no("Include numbers (0-9)? [Y/n]: ", True)
    use_special = get_yes_no("Include symbols (@#$%...)? [Y/n]: ", True)

    try:
        password = generate_password(
            length=length,
            use_uppercase=use_upper,
            use_digits=use_digits,
            use_special=use_special
        )
        print("\nGenerated Password:")
        print("------------------")
        print(password)
        print("------------------")
        print(f"Length: {len(password)} characters")
    except ValueError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()
