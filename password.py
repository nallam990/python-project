import random
import string

def generate_password(length):
    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password includes at least one character from each set
    if length < 4:
        print("Password length must be at least 4 for complexity.")
        return None

    # Generate one character from each set for a secure base
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# User Input
try:
    print("Password Generator")
    print("-------------------")
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Error: Password length must be at least 4 for a strong password.")
    else:
        password = generate_password(length)
        print(f"Generated Password: {password}")
except ValueError:
    print("Error: Please enter a valid number.")
