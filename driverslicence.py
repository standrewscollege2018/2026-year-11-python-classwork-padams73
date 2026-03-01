''' Drivers licence '''

# Set the lists
names = ["Alan", "Brianna", "Charlie", "Dora"]
status = ["No licence", "No licence", "Learners", "Restricted"]
valid_status = ["No licence", "Learners", "Restricted", "Full"]

# Start looping
change = True
while change == True:

    # Display names and status
    print("Student driver status")
    print("=" * 23)
    for i in range(len(names)):
        print(f"{i+1} {names[i]:15} {status[i]}")

    # Check that the user enters a valid selection
    # If not, print an error message
    ask = True
    while ask == True:
        try:
            driver = int(input("Select student to update: "))
            if driver < 0 or driver > len(names):
                print("Driver does not exist")
            else:
                ask = False
        except ValueError:
            print("Please enter a number")


    if driver == 0:
        change = False
    else:
        new_status = input("Enter new status: ")
        if new_status in valid_status:
            status[driver-1] = new_status
        else:
            print("Invalid status")
