'''    create a program that reads two values ​​and displays a menu on the screen:

[1] add
[2] multiply
[3] bigger
[4] new numbers
[5] exit the program'''

choice = 6

print ("Enter 2 numbers:")


while choice != 5:
    choice = 6
    while choice != 4:
        if choice == 5:
            break
        n1 = float(input("Number 1 > "))
        n2 = float(input("Number 2 > "))

        choice = 6
        while choice != 0:
            print("Menu")
            print("[1] add;")
            print("[2] multiply;")
            print("[3] bigger;")
            print("[4] new numbers;")
            print("[5] exit the program.")

            choice = int(input("Choose an option: "))

            while choice < 1 or choice > 5:
                choice = int(input("Option 1, 2, 3, 4 or 5?"))
            while choice >= 1 and choice <= 3:
                if choice == 1:
                    print (f"[1] add: {n1} + {n2} = {n1+n2}\n")
                    anything = input("Anything to go back. \n")
                    break
                if choice == 2:
                    print (f"[2] multiply: {n1} * {n2} = {n1*n2}\n")
                    anything = input("Anything to go back. \n")
                    break
                if choice == 3:
                    if n1 > n2:
                        print(f"[3] bigger:\nNumber 1: {n1} -- Number 2: {n2} >>> {n1} is bigger\n")
                    if n2 > n1:
                        print(f"[3] bigger:\nNumber 1: {n1} -- Number 2: {n2} >>> {n2} is bigger\n")
                    if n1 == n2:
                        print(f"[3] bigger:\nNumber 1: {n1} -- Number 2: {n2} >>> they are the same\n")
                    anything = input("Anything to go back. \n")
                    break         
            if choice >= 4:
                break
print ("[5] exit the program. \nBye...")
