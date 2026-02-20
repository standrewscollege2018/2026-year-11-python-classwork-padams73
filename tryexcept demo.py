''' This program demonstrates how to use try/except to handle when users enter invalid data types'''

# Because we will repeatedly ask for input until we get the correct format,
# we use a while loop
keep_asking = True
while keep_asking == True:
    
    # The code indented under try is run by the program. If there is an error
    # such as invalid data type, the program jumps immediately down to the except
    # rather than crashing the program
    try:
        number = int(input("Enter number"))
        # If the user correctly enters an integer, the program accepts it,
        # sets the value for the variable called number, then continues on
        # to the next line, where the boolean keep_asking is set to False
        # This will stop the while loop, so the program stops asking for input
        keep_asking  = False
    except ValueError:
        # Instead of crashing, the program runs this code
        # It then returns to the start of the while loop and asks for input again
        print("Not a valid integer")

print("Program continues")
