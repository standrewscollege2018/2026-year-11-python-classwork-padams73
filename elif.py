''' This program demonstrates how an else if (elif) statement works '''

# Set the number to be guessed
NUMBER = 6

# Get a guess from the user
guess = int(input("Guess a number from 1 to 10"))

# Check if guess is too low, too high, or correct
if guess < NUMBER:
    print("Too low")
elif guess > NUMBER:
    print("Too high")
else:
    print("Correct")
    