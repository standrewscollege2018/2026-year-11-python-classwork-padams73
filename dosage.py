''' Calculate paracetamol dosage'''

# Set child age limit as a constant
CHILD_AGE = 12

# Get age first
age = int(input("Enter your age in years:"))

if age >= CHILD_AGE:
    print("Take two tablets")
else:
    weight = int(input("Enter your weight in kg:"))
    dosage = weight * 10
    print(f"You should take {dosage}mg of paracetamol")

