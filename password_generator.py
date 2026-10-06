import secrets
import random
import string

MIN_LENGTH = 4
PASSWORD_FILE = "passwords.txt"


def generate_password(length: int) -> str:
    """Return a random password with at least one letter, digit and symbol."""
    if length < MIN_LENGTH:
        raise ValueError(f"Password length must be at least {MIN_LENGTH}")
    
    all_chars = string.ascii_letters + string.digits + string.punctuation

    
    chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]

    
    random.SystemRandom().shuffle(chars)
    return "".join(chars)


def save_password(password: str, filename: str = PASSWORD_FILE) -> None:
    """Append the password to a file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(password + "\n")


def get_length() -> int:
    """Keep asking until the user enters a valid length."""
    while True:
        try:
            length = int(input("Enter password length: "))
            if length >= MIN_LENGTH:
                return length
            print(f"Length must be at least {MIN_LENGTH}.")
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    length = get_length()
    password = generate_password(length)
    print("Generated Password:", password)

    if input("Save to file? (y/n): ").strip().lower() == "y":
        save_password(password)
        print(f"Saved to {PASSWORD_FILE}")


if __name__ == "__main__":
    main()

