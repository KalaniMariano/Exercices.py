'''Create a program where the user can enter seven numeric 
values ​​and register them in a single list that keeps 
even and odd values ​​separate. At the end, show the even 
and odd values ​​in ascending order.'''

print ('Type 7 integers.')

data = [[],[]]

for v in range(7):
    n = int(input(f'Value {v+1}: '))
    if n % 2 == 0:
        data[0].append(n)
    else:
        data[1].append(n)
data[0].sort()
data[1].sort()
print('=-='*20)
print(f'The EVEN values are: {data[0]}')
print(f'The ODD values are: {data[1]}')