'''create a program that reads the age and gender of multiple people. 
Every person registered in the program must decide whether or not 
the user will continue. At the end, show:
- A) How many people are over 18 years old.
- B) how many men were registered.
- C) How many women are under 20 years old.'''
cont_age = cont_men = cont_women_20 = 0
while True:
    age = int(input("Age: "))
    gender = str(input("Gender[m/f]: ").lower())
    if age >= 18:
        cont_age += 1
    if gender in ('m','men','male'):
        cont_men += 1
    if gender in ('f','female') and age < 20:
        cont_women_20 += 1
    print ('-'*50)
    reg = str(input("Do you want to continue the registration?[y/n] ").lower())
    print ('-'*50)
    if reg not in ('yes','y','s','sim'):
        break
print (f'The total of people over 18 was: {cont_age}')
print (f'The total of men registered was: {cont_men}')
print (f'The total of women under 20 was: {cont_women_20}')
   