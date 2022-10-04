'''the national swimming confederation needs a program that reads an athlete's year 
of birth and shows his category, according to age:
- up to 9 years: child
- up to 14 years: infant
- up to 19 years old: junior
- up to 20 years old: senior
- above: master'''
age = int(input("Enter age: "))
while age < 0 or age > 100:
    age = int(input("The age must be between 0 and 100: "))
if age <= 9:
    print ("Child category.")
elif age <= 14:
    print ("Infant's category.")
elif age <= 19:
    print ("Junior's category.")
elif age <= 20:
    print ("Senior's category.")
else:
    print ("Master's category.")