'''Write a program that reads two integers and compares them, displaying a message on the screen:
- the first value is higher
- the second value is higher
- there is no greater value, both are equal'''

print("Compare two numbers.")
n1 = float(input("n1: "))
n2 = float(input("n2: "))
if n1 == n2:
    print ("Both are equal.")
elif n1 > n2:
    print("The first value is higher.")
else:
    print("The second value is higher.")