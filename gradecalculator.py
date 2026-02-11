''' Calculate grades based on score from 1 to 100 '''

# Set grade boundaries
MIN_A = 90
MIN_B = 70
MIN_C = 50

# Get score from user
score = int(input("Enter your score:"))

# Calculate the grade
if score >= 0 and score <=100:
    if score >= MIN_A:
        print("A")
    elif score >= MIN_B:
        print("B")
    elif score >= MIN_C:
        print("C")
    else:
        print("Fail")
else:
    print("Invalid score. It must be between 0 and 100")
    