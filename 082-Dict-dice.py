'''Create a program where 4 players roll a dice and get random results. 
Store these results in a dictionary. In the end, put that dictionary 
in order, knowing that the winner rolled the highest number on the dice.'''
from random import randint
from time import sleep

first = second = third = fourth = 0
data = {'Player 1': randint(1, 6), 
        'Player 2': randint(1, 6), 
        'Player 3': randint(1, 6), 
        'Player 4': randint(1, 6)}

ranking = list()

print('Rolling the dice...')

for k,v in data.items():
    print(f'    {k} -> got {v}')
    sleep(0.8)
print('Ranking:')
ranking = sorted(data.items(), key=lambda item: item[1], reverse=True)
for i, v in enumerate(ranking):
    print(f'    Place {i+1} -> {v[0]} with {v[1]}')
    sleep(0.8)
