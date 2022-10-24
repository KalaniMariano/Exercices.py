'''Write a program that has a function called grades() that can receive 
multiple grades from students and will return a dictionary with the 
following information:
- Number of notes;
- The highest grade;
- The lowest grade;
- The class average;
- The situation (optional).

Also add the function docstrings.'''
def grades(lst, sit=False):
    """
    -> show the:
            - Number of notes;
            - The highest grade;
            - The lowest grade;
            - The class average;
            - The situation (optional).
    :param lst: receives the value of a list().
    :param sit: option to add the situation to the dictionary.
    :return: dictionary with the students grades.
    """
    dict_students = {}
    lower = sum_grades = bigger = situation = 0

    dict_students['Total'] = len(lst)
  
    for i in lst:
        sum_grades += i

    for b in range(len(lst)):
        if b == 0 or lst[b] > bigger:
            bigger = lst[b]

    dict_students['Bigger'] = bigger

    for l in range(len(lst)):
        if l == 0 or lst[l] < lower:
            lower = lst[l]

    dict_students['Lower'] = lower
    dict_students['Average'] = round(sum_grades/len(lst),2)

    if dict_students['Average'] < 6:
        situation = "Bad"
    else:
        situation = "Good"

    if sit == True:
        dict_students['Situation'] = situation

    return dict_students

students_grades = []

students = int(input('How many students do you want to inform the final grade? '))

for i in range(students):
    grade = float(input(f'Grade student {i+1}: '))
    while grade < 0 or grade > 10:
        grade = float(input('The grade must be between 0 and 10: '))
    students_grades.append(grade)

situation = str(input('Do you want to show the situation of the students evaluated? (y/n): ')).lower()

if situation == 'y':
    sit = True
else:
    sit = False

resp = grades(students_grades, sit)

print(resp)
