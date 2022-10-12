'''Make a program that reads the names and weights of several people, 
keeping them all in a list. At the end, show:
A) How many people were registered.
B) A list with the heaviest people.
C) A list with the lightest people.'''

name = weight = choice = cont = heaviest = lightest = 0
data = []
data_heaviest = []
data_lightest = []
while True:
    cont += 1
    name = str(input('Name: '))
    data.append(name)
    weight = float(input('Weight (kg): '))
    data.append(weight)
    choice = str(input('Do you want to continue? [y/n]'))
    if weight > heaviest or cont == 1:
        heaviest = weight
    if weight < lightest or cont == 1:
        lightest = weight
    if choice in 'Nn':
        break
for i in range(1,len(data),2):
    if data[i] == heaviest:
        data_heaviest.append(data[i-1])
    if data[i] == lightest:
        data_lightest.append(data[i-1])

print('=-='*20)
print(f'{cont} people was registered.')
print(f'The heaviest weight was {heaviest} from {data_heaviest}')
print(f'The lightest weight was {lightest} from {data_lightest}')