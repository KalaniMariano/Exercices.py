'''Write a program that has a list called numbers and two functions called draw() 
and sumEven(). The first function will select 5 numbers and place them inside 
the list and the second function will show the sum of all the EVEN values ​​drawn 
by the previous function.'''

import random
from time import sleep


def draw(lst):
    print('=-='*20)
    print('Sorting 5 values ​​from the list: ')
    for i in lst:
        sleep(0.5)
        print(f'{i}', end=' ')
    print('Done!')


def sumEven(lst):
    sum_even = 0
    for i in lst:
        if i % 2 == 0:
            sum_even += i
    print(f'Adding the EVEN values of {lst} we have: {sum_even}')


n = int(input('How many numbers do you want your list to have (equal or above 5): '))

while n < 5:
    n = int(input(f'{n} must be equal or above 5. Try again: '))

numbers = [int(input(f'Number {p+1}: ')) for p in range(n)]

draw_numbers = random.sample(numbers, 5) #sorting 5 values from de list [numbers]

draw(draw_numbers) #function draw

print('=-='*20)

sumEven(draw_numbers) #function sumEven

print('\33[32mGood bye...\33[m')
