'''Create a program that will read several numbers and put them in a list.
After that, show:
A) How many numbers were entered.
B) The list of values, sorted in descending order.
C) Whether the value 5 was entered and is or is not in the list.'''

values = []
cont = cont_5 = choice = 0
while True:
    n = int(input('Type an integer: '))
    values.append(n)
    cont += 1
    if n == 5:
        cont_5 += 1
    choice = str(input('Do you want to continue?[y/n]: '))
    if choice in ('n'):
        break

print('=-='*20)
print(f'You typed {cont} elements.')
values.sort(reverse=True)
print(f'The values in descending order: {values}')
if cont_5 > 0:
    print('5 was found in positions: ',end='')
    for i in range(len(values)):
        if 5 == values[i]:
            print(f'{i}',end=' ')
else:
    print('The value 5 is NOT part of the list')
print('=-='*20)
