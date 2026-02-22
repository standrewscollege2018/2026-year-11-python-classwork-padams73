''' Calculate a cricket batting average '''

# Set initial values for total and number of scores
total = 0
scores = 0

# Start asking repeatedly for scores until 1000 is entered
get_score = True
while get_score == True:
    score = int(input("Enter a score: "))
    if score < 0:
        print("Invalid score. Must be positive")
    elif score == 1000:
        get_score = False
    else:
        # Add score to total and add 1 to number of innings
        total += score
        scores += 1

# Check if there were no scores entered
# If so, just display a message as otherwise it would give a division by zero error
if scores == 0:
    print("No scores were entered so there is no average")
else:
    # Calculate average
    average = total / scores
    print(f"There were {scores} scores entered. The total number of runs is {total} giving an average of {average}")
