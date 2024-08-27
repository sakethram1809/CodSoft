import random
import string

def password_generator():
    print("Password Generator")

    length = int(input("Enter the desired length of the password: "))

    complexity = input("Do you want a strong password (yes/no)? ")

    if complexity.lower() == "yes":
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for i in range(length))
    else:
        password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator()