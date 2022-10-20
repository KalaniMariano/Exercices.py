'''Write a program that has a function called counter(), which takes 
three parameters: start, end and step and performs the count.

Your program has to perform three counts through the created function:

A) From 1 to 10, from 1 to 1.
B) From 10 to 0, from 2 to 2.
C) A custom count.'''
from time import sleep

def counter(* num):
    print('=-='*20)
    print('Count from 1 to 10, from 1 to 1')
    for i in range(1,11):
        print(i, end=' ')
        sleep(0.5)
    print()
    print('=-='*20)
    print('Count from 10 to 0, from 2 to 2')
    for i in range(10,-2,-2):
        print(i,end=' ')
        sleep(0.5)
    print()
    print('=-='*20)
    print("Now it's your turn to customize the count")
    a = int(input('Start: '))
    b = int(input('End: '))
    c = int(input('Step: '))
    if b < 0:
        b -= 1
    else:
        b += 1
    for i in range(a,b,c):
        print(i,end=' ')
        sleep(0.5)
counter()