
'''program that identifies if the 3 lengths of lines informed can form a triangle and 
what type of triangle is formed'''

print("Find out if the lengths of the lines form a triangle!")
a = float(input("l1: "))
b = float(input("l2: "))
c = float(input("l3: "))

if abs(b - c) < a < b + c:
    if abs(a - c) < b < a + c:
        if abs(a - b) < c < a + b:
            print ("Can form a triangle!")
else:
    print ("Can't form a triangle!")
if a == b and a == c:
    print ("Equilateral triangle.")
elif a == b or a == c:
    print ("Isosceles triangle.")
else:
    print ("Scalene triangle")