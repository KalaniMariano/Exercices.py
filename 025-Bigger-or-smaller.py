print("Type 3 numbers.")

n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))

if n1 < n2 and n1 < n3:
    print (f"{n1} is the smallest number.")
elif n2 < n3:
    print (f"{n2} is the smallest number.")
else:
    print (f"{n3} is the smallest number.")
if n1 > n2 and n1 > n3:
    print (f"{n1} is the biggest number.")
elif n2 > n3:
    print (f"{n2} is the biggest number.")
else:
    print (f"{n3} is the biggest number")

    #This code needs improvement