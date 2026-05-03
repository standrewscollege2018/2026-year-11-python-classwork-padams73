''' When search results appear they are numbered so user can select student and see all info about them '''

import sqlite3
import os
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "students.db")
 
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Start running the program
run_program = True
while run_program == True:
    # Set up empty list to hold search results
    student_results = []

    # Ask user what query they want to run
    print("Select which type of query you want to run")
    print("1. Search for student by name")
    print("2. Search for students by tutor group")
    print("3. Search for students by year group")
    print("4. Quit")
    # Error catch the selection
    get_selection = True
    while get_selection == True:
        try:
            selection = int(input())
            if selection < 1 or selection > 4:
                print("Enter 1-4 only")
            else:
                get_selection = False
        except ValueError:
            print("Enter 1-4 only")

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
        counter = 1
        for student in all_results:
            student_results.append(student)
            # create a variable that contains the first and last names
            name = f"{student[1]} {student[2]}"
            
            print(f"{counter}. {name:20} {student[3]}")
            counter += 1
        print('='*30)
        print(f"{num_results} results(s) found")

        # Ask user if they want to see all info about a student
        get_student = True
        while get_student == True:
            try:
                student_selection = int(input("Enter number of student to see all information, or enter 0 to return to main menu: "))
                if student_selection < 0 or student_selection > num_results:
                    print(f"Enter a number from 0 to {num_results}")
                else:
                    get_student = False
            except ValueError:
                print(f"Enter a number from 0 to {num_results}")
        print()
        # If the user selected a student, print their details
        # Otherwise we just return to the main menu automatically
        if student_selection != 0:
            student = student_results[student_selection-1]
            print(f"Name: {student[1]} {student[2]}")
            print(f"Tutor group: {student[3]}")
            print(f"City: {student[4]}")
            print(f"Tutor group: {student[5]}")
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

    elif selection == 3:
        # Ask use to enter a year group to search on
        year_group = input("Enter year group: ")
        # Clear a line
        print()

        # Set up and run the query
        cursor.execute("SELECT * FROM student WHERE year_group = ?",(year_group,))
        # Get results
        year_results = cursor.fetchall()
        num_results = len(year_results)
        # Display results and number found
        print(f"Students in year {year_group}")
        print("="*15)
        for student in year_results:
            print(f"{student[1]} {student[2]}")
        print("="*15)
        print(f"{num_results} result(s) found")

    else:
        run_program = False