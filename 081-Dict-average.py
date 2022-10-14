'''Make a program that reads a student's name and average, 
also storing the situation in a dictionary. At the end, 
show the content of the structure on the screen.'''

data = {}

data['NAME'] = str(input('Student NAME: '))
data['AVERAGE'] = float(input('Student AVERAGE: '))
if data['AVERAGE'] < 5:
    data['SITUATION'] = 'Disapproved'
elif data['AVERAGE'] >=5 and data['AVERAGE'] <= 6:
    data['SITUATION'] = 'Recuperation'
else:
    data['SITUATION'] = 'Approved'

for k, v in data.items():
    print(f'{k}: {v}')
