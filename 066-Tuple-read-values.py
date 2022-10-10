'''develop a program that reads 4 values ​​from the keyboard 
and stores them in a tuple. At the end, show:
A) How many times did the value 9 appear
B) In which position was the first value entered 3.
C) What were the even numbers.'''
int_number = cont9 = 0
even_number = list_numbers = ()
for v in range (4):
    n = tuple(input("Type a number: "))
    list_numbers += n
    int_number = int(list_numbers[v])
    if int_number == 9:
        cont9 += 1
    if int_number % 2 == 0:
        even_number += n
print('=-='*20)
print ('The numbers you typed were: ')
for c in range (4):
    print (f'{list_numbers[c]} > ', end='')
    if c == 2:
        c = 3
        print(f'{list_numbers[c]}')
        break
print ('1   2   3   4 -> positions')
print('-'*60)
if '3' in list_numbers:
    index3 = list_numbers.index('3')
    print(f'The number 3 appeared first in the position {index3+1}')
else:
    print ("You didn't typed the number 3")
print('-'*60)
if even_number == ():
    print ("You didn't typed an even number")
elif len(even_number) == 1:
    for even1 in range (len(even_number)):
        print (f'The even number was: {even_number[even1]}')
else:
    print ('The even numbers were: ', end='')
    for even2 in range (len(even_number)):
        print (f'{even_number[even2]} ', end='')
print('-'*60 , )
print ('Finished')