'''Write a program that has a function called area(), 
which receives the dimensions of a rectangular plot 
(width and length) and displays the area of ​​the plot.'''

def area(w,l):
    a = w * l
    print(f'The area of the rectangular plot is: {a}')


print('Choose two values ​​to calculate the area of ​​a rectangle.')

n1 = float(input('n1: '))
n2 = float(input('n2: '))

area(n1,n2)