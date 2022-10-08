'''multiplication table with break for negative number'''
i = 0
while True:
    print ("Type a negative number to stop.")
    n = int(input("Choose a number to know your multiplication table: "))
    if n < 0:
        break
    for i in range (1,11):
        print (f"{n} * {i} = {n * i}")
        if i == 10:
            print ("=-="*10)
            break
print ("Finished")