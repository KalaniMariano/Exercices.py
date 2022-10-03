import random

print ("The computer choose a number between 0 and 5, try to get it right")
n = int(input("What is your guess? "))
s = random.randrange(0,5)
p = 1
l = "("
if s == n:
    print ("You're right!!!")
else:
    while s != n:
        print (f"Wrong number :{l*p}" )
        n = int(input("Try again: "))
        p +=1
    print (f"You got it right in {p} chances!!!!!")