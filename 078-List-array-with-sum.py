
'''Enhance the previous challenge by showing at the end:
A) The sum of all even values ​​entered.
B) The sum of the values ​​in the third column.
C) The largest value of the second line.'''

array = [[],[],[]]
highest = sum_values3 = sum_values_even = 0

for l in range(0,3):
    for c in range (0,3):
        array[l].append(int(input(f'Type an integer for [{l}, {c}]: ')))
        if array[l][c] % 2 == 0:
            sum_values_even += array[l][c]
        if l == 2:
            sum_values3 += array[l][c]
        if l == 1:
            if array[l][c] > highest:
                highest = array[l][c]
print('=-='*20)
for l in range(3):
    for c in range (3):
        print(f'[{array[l][c]:^6}]',end='')
    print()
print('-'*60)
print(f'The sum of all even values ​​entered: {sum_values_even}')
print(f'The highest value of the second line: {highest}')
print(f'The sum of the values ​​in the third column: {sum_values3}')

