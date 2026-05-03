''' Program allows users to choose what query they want to run and keeps running until they choose to quit '''

import sqlite3
import os
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "students.db")
 
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Start running the program
run_program = True
while run_program == True:
    # Ask user what query they want to run
    print("Select which type of query you want to run")
    print("1. Search for student by name")
    print("2. Search for students by tutor group")
    print("3. Quit")
    # Error catch the selection
    get_selection = True
    while get_selection == True:
        try:
            selection = int(input())
            if selection < 1 or selection > 3:
                print("Enter 1-3 only")
            else:
                get_selection = False
        except ValueError:
            print("Enter 1-3 only")

    # Run the selected query
    if selection == 1:
        # Ask the user to search
        search = input("Enter search: ")
        search = f"%{search}%"

        # Set up and run a query
        cursor.execute("SELECT * FROM student WHERE first_name LIKE ? OR last_name LIKE ?",(search,search))
        # Get results
        all_results = cursor.fetchall()
        num_results = len(all_results)
        # Loop through all_results and display everyone
        print(f"{'Name':20} {'Tutor group'}")
        print('='*30)
        for student in all_results:
            # create a variable that contains the first and last names
            name = f"{student[1]} {student[2]}"
            
            print(f"{name:20} {student[3]}")
        print('='*30)
        print(f"{num_results} results(s) found")
        print()

    elif selection == 2:
        # Ask use to enter a tutor group to search on
        tutor_group = input("Enter tutor group code: ")
        # Clear a line
        print()

        # Set up and run the query
        cursor.execute("SELECT * FROM student WHERE tutor_group = ?",(tutor_group,))
        # Get results
        tutor_results = cursor.fetchall()
        num_results = len(tutor_results)
        # Display results and number found
        print(f"Students in {tutor_group}")
        print("="*15)
        for student in tutor_results:
            print(f"{student[1]} {student[2]}")
        print("="*15)
        print(f"{num_results} result(s) found")

    else:
        run_program = False