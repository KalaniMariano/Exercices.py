import random

numberstudants = int(input("How many studants do you want to draw? "))
namestudants = []
while numberstudants <= 1:
    print ("The number of students drawn must be greater than 1")
    numberstudants = int(input("Try again: "))
for i in range(numberstudants):
    names = namestudants.append(input("Name of the student: "))
random.shuffle(namestudants)
print ("The draw is:", namestudants)