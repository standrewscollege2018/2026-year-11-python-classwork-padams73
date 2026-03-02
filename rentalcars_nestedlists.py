''' Rental car program with nested lists '''

# Set up a list to store for vehicle names, seats, availability and name of renter
# I have put each vehicle's sub-list on a new line to improve readability
cars = [["Suzuki Van", 2, True, ""], 
        ["Toyota Corolla", 4, True, ""], 
        ["Honda CRV", 4, True, ""], 
        ["Suzuki Swift", 4, True, ""], 
        ["Mitsubishi Airtek", 4, True, ""], 
        ["Nissan DC Ute", 4, True, ""], 
        ["Toyota Previa", 7, True, ""],
        ["Toyota Hi Ace", 12, True, ""], 
        ["Toyota Hi Ace", 12, True, ""]]

# Run the program in a loop so user can keep making changes
run_program = True
while run_program == True:
    # Display title and list of vehicles
    print("Welcome to the University vehicle rental system")
    print("The vehicles are:")
    # Display cars in a numbered list
    for i in range(len(cars)):
        # Check if current car is available
        # Variable called status is blank if available
        if cars[i][2] == True:
            status = ""
        else:
            status = "- (Unavailable)"

        print(f"{i+1}. {cars[i][0]} ({cars[i][1]}) {status}")

    # Ask user what vehicle they want to book
    # Error catching stops them entering invalid inputs like a string or a number outside the range of the number of cars
    get_selection = True
    while get_selection == True:
        selection = int(input("What vehicle would you like to book? "))
        # If user enters 0 as their selection then the program stops asking them for a vehicle to book
        if selection == 0:
            get_selection = False
            run_program = False
        # Check if selection is in range
        elif selection < 0 or selection > len(cars):
            print(f"Number must be between 1 and {len(cars)}")
        # Check if selected car is available
        elif cars[selection-1][2] == False:
            print("*** This vehicle is already booked. Please book another ***")
        else:
            # Get their name for the booking
            # Error catch to prevent blank names
            get_name = True
            while get_name == True:
                name = input("Enter your name: ")
                if name.strip() == "":
                    print("You must enter something")
                else:
                    # Put their name in the corresponding position in the renters list so it matches the car's position
                    cars[selection-1][3] = name
                    get_name = False
            print(f"You have booked the {cars[selection-1][0]}")
            cars[selection-1][2] = False
            get_selection = False

    # Program ends by printing a summary of the rentals today
    for i in range(len(cars)):
        if cars[i][2] == False:
            print(f"{cars[i][0]} - {cars[i][3]}")