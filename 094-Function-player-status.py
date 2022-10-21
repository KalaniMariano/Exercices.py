'''Write a program that has a function called status(),
which takes two optional parameters: a player's name 
and how many goals he has scored.

The program must be able to show the player's file, 
even if some data has not been entered correctly.'''

def player_status(name='<unknown>', goals=0):
    print(f'The player {name} scored {goals} in the championship.')

n = str(input("Enter the player's name: "))
g = str(input("Number of goals: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    player_status(goals=g)
else:
    player_status(n, g)
