def multiplication():
    list[1,2,3,4,5]
    print (list)
    n = int(input("Choose a number to know your multiplication table: "))
    while n < 0 or n > 9:
        print ("The number must be between 1 and 9")
        n = int (input("Try again: "))
    for i in range (1,11):
        print (f"{n} * {i} = {n * i}")
multiplication()