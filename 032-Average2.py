'''Create a program that reads two grades from a student and calculates their average, 
showing a message at the end according to the average achieved:
- average below 5, failed
- average between 5 and 6.9, recovery
- average greater than 7, approved'''

n1 = float(input("Enter the first grade: "))
while n1 < 0 or n1 > 10:
    n1 = float(input("The grade must be between 0 and 10: "))
n2 = float(input("Enter the second grade: "))
while n1 < 0 or n1 > 10:
    n2 = float(input("The grade must be between 0 and 10: "))
a = (n1+n2)/2

if a < 5:
    print (f"You got an average of {round(a,2)}. Disapproved :(")
elif a > 5 and a < 6.9:
    print (f"You got an average of {round(a,2)}. Recovery.")
else:
    print (f"You got an average of {round(a,2)}. Approved :)")
