'''create a program that creates a 3x3 dimension matrix and fills it with values ​​read by the keyboard.
At the end, show the matrix on the screen, with the correct formatting.'''
array = [[],[],[]]
for l in range(0,3):
    for c in range (0,3):
        array[l].append(int(input(f'Type an integer for [{l}, {c}]: ')))
print('=-='*20)
for l in range(3):
    for c in range (3):
        print(f'[{array[l][c]:^5}]',end='')
    print()
