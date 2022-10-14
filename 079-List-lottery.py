'''write a program that helps a lottery player create guesses. 
The program will ask how many games will be generated and 
will draw 6 numbers between 1 and 60 for each game, 
registering everything in a composite list.'''
import random, time
print('-'*40)
print('                LOTTERY')
print('-'*40)
games = int(input('How many games do you want to draw? '))
array = [[] for c in range(games)]
for l in range(games):
    for c in range(6):
        array[l].append(random.randint(1, 60))
        for i in range(c):
            if array[l][c] == array[l][i]:
                array[l].pop(i)
                array[l].append(random.randint(1,60))
print('=-='*14)
if games == 1:
    print(f'-=-=-=- DRAWING {games} GAME -=-=-=-')
else:
    print(f'-=-=-= DRAWING {games} GAMES -=-=-=')
for l in range(games):
        array[l].sort()
        print(f'Game {l+1}: {array[l]}')
        time.sleep(1)
print(f'-=-=-=- < \33[32mGOOD LUCK!\33[m > -=-=-=-')