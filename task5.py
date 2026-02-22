''' Generate the Fibonacci series '''

# Set variables
a = 1
b = 1
c = 0

# Find out how high to count
keep_asking = True
while keep_asking == True:
    try:
        how_high = int(input("How high should we Fibonacci?"))
        keep_asking = False
    except ValueError:
        print("Please enter a positive integer")

# Print the Fibonacci series

for i in range(how_high):
    print(a)
    c = a + b
    a = b
    b = c
