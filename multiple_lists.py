''' Demonstrating how to use multiple lists '''

# Set up the lists
# The information for each person is located in the same position in each list
# For example, Abel is 25, Betty is 30, etc
names = ["Abel", "Betty", "Charles", "Dennis"]
ages = [25, 30, 19, 22]
eyes = ["Brown", "Blue", "Brown", "Grey"]

# We can then get information for a person by referring to the same index (position) in each list



# We can also format the output using f-strings, setting the width of each column
# Inside the {}, just add :width
# e.g. {names[0]:20} will make the names column 20 characters wide
for i in range(len(names)):
    print(f"{names[i]:>10} {ages[i]:8} {eyes[i]}")
