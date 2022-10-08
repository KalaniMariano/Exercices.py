'''added option for which term you want to start'''

first_term = int(input("First term of your fibonacci: "))
cont_term = int(input("How many terms do you want to view? "))

cont_while = 0

last_term = abs(first_term - 1)
next_term = 0

while cont_while < cont_term:
    print(f"{first_term} > ", end="")
    first_term = first_term + last_term
    last_term = first_term - last_term
    cont_while += 1

print("Finished")
