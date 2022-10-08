first_term = int(input("Fist term: "))
ratio = int(input("Ratio: "))
cont_term = int(input("How many terms do you want to know? "))
cont = 0
cont_term_user = 0
while cont <= cont_term:
    print (f"{first_term} > ", end='')
    first_term += ratio
    if cont == cont_term:
        cont_term_user = int(input("How many more terms do you want to show? "))
        cont -= cont_term_user
    cont += 1
print("FINISHED")

