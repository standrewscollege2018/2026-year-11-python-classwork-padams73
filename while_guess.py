''' Demonstrate while loop in a guessing game '''

import random
# Pick a random integer from 1 to 10
NUMBER = random.randint(1,10)

counter = 0

ask_guess = True

while ask_guess == True:
    # Get the guess and check if it is correct
    # If correct, set ask_guess to False
    guess = int(input("Guess a number from 1 to 10"))
    counter = counter + 1
    if guess == NUMBER:
        ask_guess = False
    elif guess < NUMBER:
        print("Too low")
    else:
        print("Too high")

print("Well done")
