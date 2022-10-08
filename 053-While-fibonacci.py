'''writes a program that reads any integer n and displays the 
first n elements of a fibonacci sequence on the screen'''

cont_term = int(input("How many terms do you want to view? "))
t1 = 0
t2 = 1
print(f"{t1} > {t2} > ", end='')
cont_while = 3
t3 = 0
while cont_while <= cont_term:
    t3 = t1 + t2
    print(f"{t3} > ", end='')
    t1 = t2
    t2 = t3
    cont_while += 1

print("Finished")