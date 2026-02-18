''' Fizzbuzz game '''

for number in range(1,31):
    # Check if it is divisble by 3. If so, print Fizz
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
