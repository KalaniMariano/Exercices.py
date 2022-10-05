#Write a program that reads any number and displays its factorial. FOR
n = int(input("Enter a number: "))
i = n
num = n

for i in range (i,1,-1):
    num = num * (i-1)

print (f"{n}! = {num}")