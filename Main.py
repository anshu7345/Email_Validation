import re

def Validation(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Validated")
    else:
        print("Please enter a correct email")

email = input("Enter your email Address: ")
Validation(email)
