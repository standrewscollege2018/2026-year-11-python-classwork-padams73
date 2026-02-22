total = 0

while total < 200:
    
    get_num = True
    while get_num == True:
        try:
            num = int(input("Enter number"))
            get_num = False
        except:
            print("Enter an integer")

    if num >=50 and num <=100:
        total += num
    else:
        print("number must be between 50 and 100")

print(total)