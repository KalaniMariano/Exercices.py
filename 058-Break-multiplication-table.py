'''multiplication table with break for negative number'''

n = int(input("Choose a number to know your multiplication table: "))
i =0
while True:
    while n > 9:
        print ("The number must be less than 9")
        n = int(input("Try again: "))
    if n < 0 or i == 10:
        break
    for i in range (1,11):
        print (f"{n} * {i} = {n * i}")