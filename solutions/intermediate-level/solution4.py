
# Implementation of email validation using regular expressions
import re


def validate_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # If the string is empty
    if email == "":
        return False
    
    # If the string is not empty
    if re.match(regex, email):
        return True
    else:
        return False
    

# Example usage
email = "test@domain.com"
print(validate_email(email))  # Output: True
email = "invalid-email"
print(validate_email(email))  # Output: False