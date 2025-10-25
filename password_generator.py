import random
import string

def generate_password(length=12, use_special_chars=True):
    """Generate a random password."""
    if length < 4:
        print("Password length should be at least 4.")
        return None

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = letters + digits + special_chars

    # Ensure password has at least one letter, one digit, and one special character (if used)
    password = [
        random.choice(letters),
        random.choice(digits)
    ]

    if use_special_chars:
        password.append(random.choice(special_chars))

    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)


if __name__ == "__main__":
    print("=== Password Generator ===")
    length = int(input("Enter password length: "))
    special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, special)
    if password:
        print(f"Generated Password: {password}")
