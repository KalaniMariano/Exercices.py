'''Enhance challenge 084 to work with multiplayer, 
including a system to view each player's performance details.'''

data_player = {}
data_everyone = []
goals_list = []
total_goals = cont_len_goals = cont_game = 0
total_len = 13
players = int(input('How many players do you want to register? '))
for p in range(players):
    print(f'-=-=-= < Player {p+1} > =-=-=-')
    data_player['Name'] = str(input('Type de player name: '))
    matches = int(input('How many matches were played? '))
    while matches <= 0:
        matches = int(input('Please choose at least 1 the number of matches: '))
    for i in range(matches):
        goals = int(input(f'How many goals in match {i+1}: '))
        goals_list.append(goals)
        total_goals += goals
    average = round(total_goals/matches,2)
    data_player['Goals'] = goals_list.copy()
    goals_list.clear()
    data_player['Total'] = total_goals
    total_goals = 0
    data_player['Average'] = average
    data_everyone.append(data_player.copy())
    data_player.clear()
print('=-='*20)
print(data_everyone)
print('=-='*20)
print('Nº Name          Goals          Total Average')
print('-'*45)
for i, v in enumerate(data_everyone):
    print(f'{i+1}  {(data_everyone[i]["Name"]):<14}',end='')
    for l in range(len(data_everyone[i]['Goals'])):
        print(f'{data_everyone[i]["Goals"][l]}',end=' ')
        cont_len_goals += 1
    print(' '*((total_len-cont_len_goals)-(cont_len_goals-1)), f'{(data_everyone[i]["Total"]):^3}{(data_everyone[i]["Average"]):>8}')
    cont_len_goals = 0
print('-'*45)
while True:
    choice = int(input('Do you want to show the data of which player? (\33[31m999 to finalize\33[m): '))
    choice -= 1
    while choice >= len(data_everyone) and choice < 998 or choice > 999:
        print('Oops this player does not exist. Try again.')
        choice = int(input('Do you want to show the data of which player? (\33[31m999 to finalize\33[m): '))
        choice -= 1
    if choice == 998:
        break
    print (f'-- {data_everyone[choice]["Name"]} stats:')
    for l in range(len(data_everyone[choice]['Goals'])):
        cont_game += 1
        print(f'      In the game {cont_game} he scored {data_everyone[choice]["Goals"][l]} goals')
    print(f'Total of {data_everyone[choice]["Total"]} goals and a average of {data_everyone[choice]["Average"]} goals per match')
    cont_game = 0
    print()    
print('\33[32mGood bye...\33[m')