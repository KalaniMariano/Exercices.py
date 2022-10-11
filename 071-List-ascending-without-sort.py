'''create a program where the user can type five numeric 
values ​​and register them in a list, already in the 
correct insertion position (without using sort()).
At the end show the sorted list on the screen'''

n = 0
values = []
for i in range (5):
    n = int(input('Type an integer: '))
    if i == 0 or n >= values[-1]:
        values.append(n)
        print('Added at the end of the list...')
    else:
        for v in range(len(values)):
            if n <= values[v]:
                values.insert(v, n)
                print (f'Inserted in position \033[32m{v+1}\33[m')
                break
print(values)