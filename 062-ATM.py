'''create a program that simulates the operation of an ATM. 
At the beginning, ask the user what will be the amount 
to withdraw (integer) and the program will inform you 
how many bills of each amount will be delivered.
NOTE: Consider that the cashier has $50, $20, $10 and $1 bills'''
rest = bills_50 = bills_20 = bills_10 = bills_1 = 0

n = int(input('What is the amount to be withdrawn? $'))
rest = n
if rest >= 50:
    bills_50 = n // 50
    rest = n % 50
if rest >= 20:
    bills_20 = rest // 20
    rest %= 20
if rest >= 10:
    bills_10 = rest // 10
    rest %= 10
if rest >= 1:
    bills_1 = rest // 1
    rest %= 1
print (f'\033[32m{bills_50}\033[m $50 bills, \033[32m{bills_20}\033[m $20 bills, \033[32m{bills_10}\033[m $10 bills and \033[32m{bills_1}\033[m $1 bills.')
    