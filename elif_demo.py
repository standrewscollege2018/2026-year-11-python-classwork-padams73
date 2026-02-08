''' This program demonstrates how to write an elif statement by running asking
the user to guess a number and returning whether they are too high, low or correct'''

guess = int(input("Guess a number from 1 to 10"))

if guess < 6:
    print("Too low")
elif guess > 6:
    print("Too high")
else:
    print("Correct")


    
