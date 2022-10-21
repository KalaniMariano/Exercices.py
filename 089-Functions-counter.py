'''Write a program that has a function called counter(), which takes 
three parameters: start, end and step and performs the count.

Your program has to perform three counts through the created function:

A) From 1 to 10, from 1 to 1.
B) From 10 to 0, from 2 to 2.
C) A custom count.'''
from time import sleep

def counter(i,f,p):
    print('=-='*20)
    if p == 0: #if step == 0
        p += 1 #add 1 to step

    if i > f and p > 0: #if the start is greater than the end and step is > 0, the step needs to be decreasing
        p *= -1         #so multiply the step by -1
    if i < f and p < 0: #same concept as the last "if"
        p *= -1         
    print(f'Count from {i} to {f}, from {p} to {p}')

    if p < 0:   #this "if" is for the "for" show the number that the user entered for the "end"
        f -= 1
    else:
        f += 1

    for x in range(i,f,p):
        print(x,end=' ')
        sleep(0.2)

    print('\33[32mTHE END...\33[m')


counter(0,10,1)
counter(10,0,1)
print("Now it's your turn to customize the count")
a = int(input('Start: '))
b = int(input('End: '))
c = int(input('Step: '))
counter(a,b,c)