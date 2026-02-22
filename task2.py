''' Get two numbers, the second of which must be greater than the first '''

# Get first number
number1 = int(input("Enter the first number: "))

# Get the second number
# Using a while loop to keep asking until the user gives a number greater than the first
get_num = True
while get_num == True:
    number2 = int(input("Enter a number greater than the first one: "))
    if number2 > number1:
        get_num = False
    else:
        print(f"That is not greater than {number1}")

print(f"Thanks. The numbers you entered were {number1} and {number2}")
