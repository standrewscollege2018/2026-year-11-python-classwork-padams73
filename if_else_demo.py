''' Demonstrating how a conditional statement (if/else) works
It asks the user for a password and then checks if it is correct'''

# Set password as a constant (because it doesn't change)
SAVED_PASSWORD = "carrots"

# Ask for password and store in a variable
password = input("Enter your password")

# Check if it is correct
if password == SAVED_PASSWORD:
    print("Correct password")
else:
    print("Incorrect. Get out!")



