import re
import random

def check_password_strength(password):
    """Calculates and returns a password strength rating."""

    score = 0
    length = len(password)

    if length >= 12:
        score += 5
    elif length >= 8:
        score += 3
    elif length >= 6:
        score += 1

    if re.search("[a-z]", password):
        score += 2
    if re.search("[A-Z]", password):
        score += 2
    if re.search("[0-9]", password):
        score += 2
    if re.search(r"[!@#$%^&*()_+=\\[\]{};':\"\\|,.<>\/?] ", password):  # Using a raw string
        score += 2

    if score >= 10:
        return "Strong"
    elif score >= 6:
        return "Medium"
    else:
        return "Weak"

def generate_strong_password(length=12):
    """Generates a strong random password."""

    characters = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=\\[\]{};':\"\\|,.<>\/?"  # Using a raw string
    password = ''.join(random.sample(characters, length))
    return password

# Main loop for user interaction
while True:
    print("\nChoose an option:")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")

    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        password = input("Enter a password: ")
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")
        if strength == "Weak" or strength == "Medium":
            print("Suggestion: Try using a longer password with a mix of lowercase, uppercase, numbers, and symbols.")

    elif choice == '2':
        length = int(input("Enter desired password length: "))
        strong_password = generate_strong_password(length)
        print(f"Generated strong password: {strong_password}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

    # Ask the user if they want to continue
    continue_choice = input("\nDo you want to continue? (1. Yes, 2. No): ")
    if continue_choice != '1':
        break

print("Exiting the password tool. Goodbye!")
