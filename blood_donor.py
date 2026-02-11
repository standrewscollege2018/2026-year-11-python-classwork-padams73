''' Blood donor program, checking age and weight for eligibility '''

# Set restrictions
MIN_AGE = 16
MIN_WEIGHT = 50

# Get info from user
age = int(input("Enter your age:"))
# Using float as users might enter decimals for their weight
weight = float(input("Enter your weight:"))

# Check if eligible
if age >= MIN_AGE and weight >= MIN_WEIGHT:
    print("Eligible")
else:
    print("You are not eligible to give blood")
