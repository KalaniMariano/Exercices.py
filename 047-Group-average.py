'''develop a program that reads the name, age and gender of 4 people. At the end of the program it shows:
- the mean age of the group
- what is the name of the oldest man
- how many women are under 20'''

sum_average = 0
name_oldest = ''
sum_women = 0

print ("Enter the NAME, AGE and GENDER of 4 people.")

for i in range (1,5):
    print (f"Person {i}")
    name = str(input("NAME: "))
    age = int(input("AGE: "))
    gender = str(input("M or W? "))
    print ('\n')
    
    sum_average += age

    if i == 1 and gender in ('M','m'):
        name_oldest = name
    if gender in ('W','w'):
        if age < 20:
            sum_women += 1
print (f'The mean age of the group: {sum_average/i}')
print (f'The name of oldest Man: {name_oldest}')
print (f'How many women are under 20: {sum_women}')