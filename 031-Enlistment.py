'''Make a program that reads the year of birth of a young person and reports, according to their age:
- if he's still going to enlist in the military.
- if it's time to enlist.
- if it is past the time of enlistment
'''

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
year = int(year)
birth = int(input("Type your year of birth: "))
age = year - birth
while age <= 0 or age > 120:
    birth = int(input("The year entered is wrong, try again: "))
if age < 17:
    print(f"You will enlist in {18-age} years.")
elif age == 18:
    print("It's time to enlist.")
else:
    print(f"Did you enlist or should have enlisted {age-18} year(s) ago in {year-(age-18)}")
