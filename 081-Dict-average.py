'''Make a program that reads a student's name and average, 
also storing the situation in a dictionary. At the end, 
show the content of the structure on the screen.'''

data = {}
student = []

data['NAME'] = str(input('Student NAME: '))
data['AVERAGE'] = float(input('Student AVERAGE: '))
if data['AVERAGE'] < 5:
    data['SITUATION'] = 'Disapproved'
elif data['AVERAGE'] >=5 and data['AVERAGE'] <= 6:
    data['SITUATION'] = 'Recuperation'
else:
    data['SITUATION'] = 'Approved'

student.append(data.copy())

for e in student:
    for k, v in e.items():
        print(f'{k}: {v}')
