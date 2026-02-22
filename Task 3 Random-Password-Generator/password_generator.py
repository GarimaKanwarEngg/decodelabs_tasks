"""
Random Password Generator
Author: Your Name
Description: A secure, function-based random password generator using Python.
"""

import random
import string


def validate_length(length_input):
    """
    Validates user input for password length.
    Ensures:
    - Input is numeric
    - Length is at least 8 (recommended minimum for security)
    """
    if not length_input.isdigit():
        raise ValueError("Password length must be a number.")

    length = int(length_input)

    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")

    return length


def generate_password(length):
    """
    Generates a strong random password.
    
    Ensures password contains:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """

    # Define character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Combine all characters
    all_characters = uppercase + lowercase + digits + special

    # Ensure password contains at least one character from each required category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the remaining length randomly
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)


def main():
    """
    Main execution function.
    Handles user input and displays generated password.
    """

    print("\n🔐 Random Password Generator")
    print("--------------------------------")

    try:
        user_input = input("Enter desired password length (minimum 8): ")
        length = validate_length(user_input)

        password = generate_password(length)

        print("\n✅ Generated Secure Password:")
        print(password)

    except ValueError as error:
        print(f"\n❌ Error: {error}")


if __name__ == "__main__":
    main()