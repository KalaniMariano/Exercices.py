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
    data.append([name, [grade1, grade2]])
    average.append(round(((grade1+grade2)/2),2))
    choice = str(input('Do you want to continue?[y/n]: '))
    cont += 1
    if choice in 'Nn':
        break
print('=-='*20)
print('Nº        NAME        AVERAGE')
print('-----------------------------')
for i in range(cont):
        print(f'{i+1}{data[i][0]:^20}    {average[i]:^5}')
while True:
    student = int(input('Do you want do see the grades of which student?(\33[31m0 to finalize\33[m): '))
    if student == 0:
        print('\33[31mEnding the program...\33[m')
        break
    print(f'Student {student} - {data[student-1][0]}\nGrade 1: {data[student-1][1][0]}\nGrade 2: {data[student-1][1][1]}')

