'''Create a program that manages the use of a football player. 
The program will read the player's name and how many matches 
he played. Then you will read the number of goals scored in 
each match. In the end, all this will be stored in a dictionary, 
including the total goals scored during the championship.'''

data = {}
goals_list = []
total_goals = 0
data['Name'] = str(input('Type de player name: '))
matches = int(input('How many matches were played? '))
for i in range(matches):
    goals = int(input(f'How many goals in match {i+1}: '))
    goals_list.append(goals)
    total_goals += goals
data['Goals'] = goals_list.copy()
data['Total'] = total_goals
print('=-='*20)
print(data)
print('=-='*20)
for k, v in data.items():
    print(f'{k} has value of {v}')
print('=-='*20)
if matches == 1: 
    print(f'The player {data["Name"]} played {matches} match.')
else:
    print(f'The player {data["Name"]} played {matches} matches.')
for pos, v in enumerate(goals_list):
    if v == 1:
        print(f'    -> In match {pos+1}, scored {v} goal.')
    else:
        print(f'    -> In match {pos+1}, scored {v} goals.')
if data['Total'] == 0:
    print('Did not score any goals.')
if data['Total'] == 1:
    print(f'It was a total of {data["Total"]} goal.',end=' ')
else:
    print(f'It was a total of {data["Total"]} goals.',end=' ')
average = round(data["Total"]/matches,2)
if average == 1:
    print(f'With an average of {average} goal per match.')
else:
    print(f'With an average of {average} goals per match.')