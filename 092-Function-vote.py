'''Create a program that has a function called vote() that will receive 
a person's year of birth as a parameter, returning a literal value 
indicating whether a person has a DENIED, OPTIONAL or MANDATORY vote 
in the elections.'''
import datetime

current_year = datetime.datetime.now().year

def vote(year):
    age = current_year - year
    if age < 16:
        status = "DENIED"
    if (age >=16 and age < 18) or age >= 70:
        status = "OPTIONAL"
    if age >= 18 and age < 70:
        status = "MANDATORY"
    print(f'At {age} years old. The vote is >>> {status}')

year_of_birth = int(input('What year were you born? '))

vote(year_of_birth)