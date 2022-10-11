'''Create a program that will read several numbers and put them in a list.
After that, create two extra lists that will contain only the even values 
​​and the odd values ​​entered, respectively.
At the end show the content of the 3 generated lists'''

values = []
values_even = []
values_odd = []
while True:
    n = int(input('Type an integer: '))
    values.append(n)
    choice = str(input('Do you want to continue?[y/n]: '))
    if choice in ('n'):
        break

for v in range(len(values)):
    if values[v] % 2 == 0:
        values_even.append(values[v])
    else:
        values_odd.append(values[v])

print('=-='*20)
print(f'Original list: {values}')
print(f'List with EVEN numbers: {values_even}')
print(f'List with ODD numbers: {values_odd}')

