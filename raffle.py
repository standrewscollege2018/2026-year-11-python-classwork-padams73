''' This program simulates a raffle '''

# Import the random package so we can choose a winner at random
import random
# Import time package so we can create drama
import time

# Set the empty list to hold raffle entries
entries = []

# Print out a greeting
print("Welcome to the Raffle program")

# Get the prize and its value
# Error catching to prevent blank prizes
get_prize = True
while get_prize == True:
    prize = input("What is the prize being raffled? ")
    # .strip() removes any spaces
    if prize.strip() == "":
        print("No blanks allowed")
    else:
        get_prize = False

# Error catching to ensure we get a value that is integer and positive
get_value = True
while get_value == True:
    try:
        value = int(input(f"What is the value of the {prize}? (do not enter the $ sign)"))
        if value <= 0:
            print("Value must be positive")
        else:
            get_value = False
    except ValueError:
        print("Value must be a positive integer")

# Start asking for names to enter the raffle
get_names = True
while get_names == True:
    name = input("Enter name of entrant: ")
    # Checking for blank entries
    if name.strip() == "":
        print("No blanks allowed")
    # Check if name is already entered
    elif name in entries:
        print("They are already entered in the raffle")
    # If 'end' is entered, we stop asking
    elif name == "end":
        get_names = False
    else:
        entries.append(name)

# If there are people entered, we run the draw
if len(entries) > 0:
    # State how many people are in the draw
    print(f"There are {len(entries)} people in the draw for the {prize}")

    # Randomly select someone from the entries list
    winner = random.randint(0,len(entries)-1)
    print(f"And the winner of the {prize} valued at ${value} is...")
    time.sleep(2)
    print(f"{entries[winner]}")
else:
    print("No one entered the raffle")