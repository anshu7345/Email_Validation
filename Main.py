import re

def validate_email(email):
    # Improved regular expression for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(pattern, email):
        print("Email is valid.")
    else:
        print("Please enter a valid email address.")

def main():
    print("Welcome to the Email Validation Program")
    print("-------------------------------------")
    
    while True:
        email = input("Enter your email address (or type 'exit' to quit): ")
        
        if email.lower() == 'exit':
            print("Exiting the program.")
            break
        
        validate_email(email)
        print()

if __name__ == "__main__":
    main()
