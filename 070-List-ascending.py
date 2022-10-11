'''create a program where the user can enter several numeric 
values ​​and register them in a list. If the number already 
exists in there, it will not be added. At the end, all 
unique values ​​entered will be displayed, in ascending order'''
choice = n = 0
values = []

while True:
    n = int(input('Type an integer: '))
    if n not in values:
        values.append(n)
    choice = str(input('Do you want to continue? [y/n]: '))
    if choice in ('n'):
        break
values.sort()   
print(values)
