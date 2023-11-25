import random
import string


def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Example usage
password = generate_password(8)
# Generates a password with default length of 8
print(password)

password = generate_password(12)  # Generates a password with length of 12
print(password)
