'''create a program that reads the birth year of seven people. At the end, show how many 
people have not yet reached the age of majority and how many are over 18 years old.'''
import time

friends = 0
criminal_majority = 0

cont_friends = 0
age = 0
drive = 0
drive_and_criminal_majority = 0
in_criminal_majority = 0
not_majority = 0

prompt = "How many friends do you want to verify the age? "
prompt2 = "How old is the age of criminal responsibility in your state? "
prompt3 = "Enter age: "

while True:
    try:
        friends = int(input(prompt))
    except:
        print ("Only numbers. Try again... ")
        continue
    if friends <= 0:
        print ("Number of friends to verify can't be less than 0.")
        prompt = "Try again: "
    else:
        break
    

while True:
    try:
        criminal_majority = int(input(prompt2))
    except:
        print ("Only numbers. Try again... ")
        continue
    if criminal_majority < 12 or criminal_majority > 18:
        print ("The age of criminal responsibility in the USA is between 12 and 18 years old.")
        prompt2 = "Try again: "
    else:
        break


for i in range(friends):
    cont_friends += 1
    print (f"\nFriend number {cont_friends}!")
    while True:
        try:   
            age = int(input(prompt3))
        except:
            print ("Only numbers. Try again...")
            continue
        if age <= 0 or age > 100:
            print ("The age must be between 0 and 100.")
            prompt3 = "Try again: "
        else:
            break
    if age < criminal_majority and age >= 16: #only drive
        drive += 1
    if age >= criminal_majority and age >= 16: #drive and criminal majority
        drive_and_criminal_majority += 1
    if age >= criminal_majority and age < 16: #criminal majority only
        in_criminal_majority += 1
    if age < criminal_majority and age < 16: #not in majority and not drive
        not_majority += 1

print("\nVerifying...")
time.sleep(1.5)
print(f"{not_majority} - Not in criminal majority and can't drive;")
print(f"{drive} - Can only drive;")
print(f"{in_criminal_majority} - Only in criminal majority;")
print(f"{drive_and_criminal_majority} - Can drive and are in criminal majority.")