'''Create a program that reads the name, sex and age of several people, 
storing each person's data in a dictionary and all dictionaries in a list. 
At the end, show:
A) How many people were registered.
B) The average age of the group.
C) A list of all women.
D) A list of all people above average age.'''

data_people = {}
data_everyone = []
all_women = []
above_average = []

cont_peoples = sum_age = cont_women = cont_above_average = 0
while True:
    cont_peoples +=1
    print(f'-=-=-= < Record {cont_peoples} > =-=-=-')
    data_people['Name'] = str(input('Name: '))
    data_people['Gender'] = str(input('Gender (M/F): ')).upper()
    if data_people['Gender'] in 'F':
        cont_women += 1
        all_women.append(data_people['Name'])
    data_people['Age'] = int(input('Age: '))
    sum_age += data_people['Age']
    choice = str(input('Enter "n" to stop, anything else to continue: ')).lower()
    data_everyone.append(data_people.copy())
    if choice in 'n':
        break
average = round(sum_age/cont_peoples,2)
print('=-='*20)
print(data_everyone)
print('=-='*20)
if cont_peoples == 1:
    print(f'- {cont_peoples} person has been registered.')
else:
    print(f'- {cont_peoples} people have been registered.')
print(f'- The average age of the group is {average}.')
if cont_women > 0:
    print('- List of all women: ',end='')
    for i in range(cont_women):
        print(all_women[i], end=' ')
    print()
else:
    print('- No women were registered.')
for v in range(len(data_everyone)):
    if data_everyone[v]['Age'] > average:
        above_average.append(data_everyone[v])
    if data_everyone[v]['Age'] == average:
        cont_above_average +=1
if cont_above_average == cont_peoples:
    print('- There is no one above average age.')
else:
    print('- List of all people above average age: ')
    for pos, v in enumerate(above_average):
        print(f'    {pos+1}. Name: {v["Name"]} - Gender: {v["Gender"]} - Age: {v["Age"]}')
print('Ending...')

        