'''make a program that reads 5 numeric values ​​and stores them in a list.
At the end, show what was the highest and lowest value entered and 
their respective positions in the list.'''

lower = highest = n = 0
values = []

for v in range (5):
    n = int(input("Type an integer: "))
    values.append(n)
    if n < lower or v == 0:
        lower = n
    if n > highest or v == 0:
        highest = n

print('=-='*20)
print(f'You typed the values: {values}')
print ('Positions -----------> 1  2  3  4  5')
print('=-='*20)
print(f'The highest value is {highest} and it appeared in position(s): ',end='')

for pos, h in enumerate(values):
    if values[pos] == highest:
        print (pos+1, end=' ')

print(f'\nThe lowest value is {lower} and it appeared in position(s): ',end='')
for pos, l in enumerate(values):
    if values[pos] == lower:
        print (pos+1, end=' ')
print('')
print('=-='*20)