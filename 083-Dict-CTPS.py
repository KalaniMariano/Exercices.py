'''Create a program that reads name, year of birth and work card 
and registers them (with age) in a dictionary if by chance the 
CTPS is different from ZERO, the dictionary will also receive 
the year of hire and salary. Calculate and add, in addition to 
age, at what age the person will retire. Consider that to retire 
you need 35 years of contribution.'''
import datetime

data = {}
current_year = datetime.datetime.now().year

data['Name'] = str(input('Name: '))
year_of_birth = int(input('Year of birth: '))
data['Age'] = current_year - year_of_birth
data['CTPS'] = int(input('CTPS (0 for not have): '))
if data['CTPS'] != 0:
    data['Hire'] = int(input('Year of hire: '))
    data['Salary'] = str(input('Salary: '))
    data['Retirement'] = data['Hire'] - year_of_birth + 35
print('=-='*20)
for k, v in data.items():
    print(f'{k} has value of {v}')
