'''create a program that will generate five random numbers and put them in a tuple.
After that, show the generated numbers listing and also indicate the smallest 
and largest value that is in the tuple'''
import random
x = [random.randint(0, 1000) for p in range(0, 5)]
smallest = bigger = 0
print (f'Random numbers generated: \n{x}')
print ('=-='*15)
for s in range (5):
    if x[s] < smallest or s == 0:
        smallest = x[s]
for b in range (5):
    if x[b] > bigger or s == 0:
        bigger = x[b]
print(f'The smallest number is: {smallest}')
print(f'The biggest number is: {bigger}')