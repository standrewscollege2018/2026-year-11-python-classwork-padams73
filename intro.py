''' This program demonstrates print(), data types, variables, inputs and f-strings'''

# print() is a function that outputs whatever is inside the brackets
# numbers can be included directly in the brackets
print(123)
print(1.5)

# when printing text, it must be in speechmarks which turns it into a string
print("Hello")

# There are lots of different data types:
# integers, decimals (floating point numbers)
# text (string), boolean (true or false)

# We use variables to store information
# variables must be all lower case
# if you want multiple words in the variable name, use underscore
name = "Pluto"
first_name = "John"
last_name = "Smith"
age = 14

# You can include variables inside print() statements
print(name)
# To combine variables with a string, we use f-strings
# The variable goes inside curly brackets {}
print(f"My dog is called {name} and he is {age} years old")

# We use input() to get input from the user
user_name = input("What is your name?")

# Print hello to the user and ask them how old they are
user_age = input(f"Hi {user_name}, how old are you?")

# Then print out their name and age
print(f"You are {user_name} and you are {user_age} years old")
