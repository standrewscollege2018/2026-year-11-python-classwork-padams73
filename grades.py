''' This program asks for a score between 0 and 100 and then gives a grade'''

keep_asking = True

while keep_asking == True:

    score = int(input("Enter you score from 0 to 100: "))

    if score >= 0 and score <= 100:
        keep_asking = False

    else:
        print("Oops! You entered an invalid score. It must be from 0 to 100.")

# Calculate the grade based on the score the user entered
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >=50:
    print("C")
else:
    print("Fail")
