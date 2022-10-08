first_term = int(input("Fist term: "))
ratio = int(input("Ratio: "))
cont_term = int(input("How many terms do you want to know? "))
cont = 0
while cont < cont_term:
    print (f"{first_term} > ", end='')
    first_term += ratio
    cont += 1
print("FINISHED")

'''for i in range (term,n,ratio):
        print ("{} ".format(i), end=' > ')
print ("FINISHED")'''   