'''Write a program that has a function called greater(), which takes several parameters with integer values.

Your program has to analyze all the values ​​and say which one is the biggest.'''
from time import sleep

def greater(lst):
    greater_num = 0
    for i in range(len(lst)):
        if i == 0 or lst[i] > greater_num:
            greater_num = lst[i]
    print('=-='*20)
    print('Analyzing the values ​​passed', end='')
    for i in range(len(lst)+2):
        sleep(0.2)
        print('.',end='')
    print()
    for i in lst:
        print(i,end=' ')
    if len(lst) == 1:
       print(f'- Was informed {len(lst)} value.')
    else:
        print(f'- Were informed {len(lst)} values.')
    print(f'The highest number was {greater_num}')
    print('=-='*20)


nums_list = []
while True:
    nums = int(input('How many numbers do you want to write? '))
    for i in range(nums):
        n = int(input(f'Number {i+1}: '))
        nums_list.append(n)
    greater(nums_list)
    nums_list.clear()
    choice = str(input('Type "n" to end the program, anything else to continue: '))
    if choice in 'Nn':
        print('\33[32mGood bye...\33[m')
        break
    print('-'*60)