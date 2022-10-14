'''Create a program that reads the name and two grades 
of several students and stores them all in a composite 
list. At the end, show a report card containing the 
average of each one and allow the user to see the grades 
of each student individually.'''

cont = grade1 = grade2 = 0
data = []
names = []
grades = []
average = []
while True:
    name = str(input(f'Student {cont+1}: '))
    grade1 = float(input('Grade 1: '))
    while grade1 < 0 or grade1 > 10:
        grade1 = int(input('This number must be between 0 and 10: '))
    grade2 = float(input('Grade 2: '))
    while grade2 < 0 or grade2 > 10:
        grade2 = int(input('This number must be between 0 and 10: '))
    names.append(name)
    data.append(names[:])
    names.clear()
    grades.append(grade1)
    grades.append(grade2)
    data[cont].append(grades[:])
    grades.clear()
    average.append((grade1+grade2)/2)
    choice = str(input('Do you want to continue?[y/n]: '))
    cont += 1
    if choice in 'Nn':
        break
print('=-='*20)
print('Nº        NAME        AVERAGE')
print('-----------------------------')

for i in range(cont):
    print(f'{i+1}{data[i][0]:^20}    {average[i]:^5}')


