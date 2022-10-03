import math 

oside = float(input("Opposite side: "))
while oside <= 0:
    print ("Opposite side must be grater than 0")
    oside = float(input("Try again: "))

aside = float(input("Adjacent side: "))
while aside <= 0:
    print ("Ajacent side must be grater than 0")
    aside = float(input("Try again: "))

h = math.hypot(oside,aside)
print (h)