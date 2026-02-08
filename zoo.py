''' Check whether the user pays the child price when they visit the zoo'''

# Set the child age value
CHILD_AGE = 13

# Ask for age
age = int(input("Enter your age"))

# Check if they are a child or not
if age < CHILD_AGE:
    print("You may the child price")
else:
    print("You pay full price")

print("Welcome to the zoo")
