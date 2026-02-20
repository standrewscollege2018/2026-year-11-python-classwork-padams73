best_score = 9999999999

import random

keep_playing = True

while keep_playing == True:
    
    number = random.randint(1,10)

    score = 0

    keep_guessing = True

    while keep_guessing == True:

        score = score + 1

        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Correct!")
            keep_guessing = False
        elif guess < number:
            print("Too low")
        else:
            print("Too high")

    print(f"You took {score} guesses")
    if score < best_score:
        print("You got the new best score!")
    else:
        print(f"The best score is still {best_score}")
    again = input("Play again? (y/n")
    if again == "n":
        keep_playing = False
