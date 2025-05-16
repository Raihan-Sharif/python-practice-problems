
def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_upper and has_lower and has_digit and has_special

def main():
    pwd = input("Enter password: ")
    if is_valid_password(pwd):
        print("Valid password.")
    else:
        print("Invalid password. Must be at least 8 chars, include upper, lower, digit, and special char.")

if __name__ == "__main__":
    main()

