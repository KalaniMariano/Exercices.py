#Write a program that reads any number and displays its factorial. WHILE

n = float(input("Enter a number: "))
num = n
cont_num = num
while cont_num != 1:
    num = num * (cont_num - 1)
    cont_num -= 1

print (f"{n}! = {num}")