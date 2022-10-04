#develop a program that reads six integers and displays the sum of only those that were even

s = 0
for i in range (0,6):
    n = int(input("Type a number: "))
    if n % 2 == 0:
        s += n
print (f"The sum of the even numbers you entered was: {s}")