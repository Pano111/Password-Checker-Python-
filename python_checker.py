import re
import random
import string

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Weak: Add at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Weak: Add at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Weak: Add at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Add at least one special character."
    return "Strong"

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


while True:
    password = input("Enter a password (or type 'generate' to get a strong one): ")

    if password.lower() == "generate":
        new_password = generate_strong_password()
        print(f"🔑 Here is a strong password for you: {new_password}")
        break

    result = check_password_strength(password)
    if result == "Strong":
        print("✅ Your password is strong!")
        break
    else:
        print(result)
        print("❌ Try again or type 'generate' to get one.\n")
