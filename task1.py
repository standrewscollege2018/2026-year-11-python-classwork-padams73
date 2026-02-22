''' Get two numbers, compare them and print them '''

# Get two numbers
num1 = int(input("Enter a number:"))



num2 = int(input("Enter a number:"))

# Compare the numbers and print the result
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")