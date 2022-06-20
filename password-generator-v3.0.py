import re
import time
import string
import secrets


def generate():
    try:
        length, uppercase, lowercase, digits, symbols = check_inputs()

        alphabet = uppercase + lowercase + digits + symbols

        while True:
            password = "".join([secrets.choice(alphabet) for _ in range(length)])
            if check_password(password, uppercase, lowercase, digits, symbols):
                break
        print(password)

    except TypeError:
        return


def check_inputs():
    try:
        length = int(input("Enter the password length between 12 and 128 characters: "))

        if length < 12:
            length = 12

        if length > 128:
            length = 128

    except ValueError:
        print("\nInvalid password length. Please try again.")
        return

    uppercase = string.ascii_uppercase if "y" in input("Should your password include uppercase letters? (y/n): ") else ""
    lowercase = string.ascii_lowercase if "y" in input("Should your password include lowercase letters? (y/n): ") else ""
    digits = string.digits if "y" in input("Should your password include digits? (y/n): ") else ""
    symbols = "!@#$%^&*" if "y" in input("Should your password include symbols? (y/n): ") else ""

    if all(not _ for _ in [uppercase, lowercase, digits, symbols]):
            uppercase = string.ascii_uppercase
            lowercase = string.ascii_lowercase
            digits = string.digits

    return length, uppercase, lowercase, digits, symbols


def check_password(password, uppercase, lowercase, digits, symbols):
    uppercase_error = re.search(r"[A-Z]", password) is None if uppercase else False
    lowercase_error = re.search(r"[a-z]", password) is None if lowercase else False
    digit_error = re.search(r"\d", password) is None if digits else False
    symbol_error = re.search(r"[!@#$%^&*]", password) is None if symbols else False
    return not (uppercase_error or lowercase_error or digit_error or symbol_error)


if __name__ == "__main__":
    generate()
    time.sleep(30)
