'''create a program that reads the name and price of multiple products. 
The program should ask if the user is going to continue. At the end, show:
- A) What is the total spent on the purchase.
- B) How many products cost more than R$1000.
- C) What is the name of the cheapest product.'''
choice = 0
cheapest = 0
cheapest_name = 'x'
cont = 0
total = 0
cont_cost = 0
while True:
    name = str(input("Name of the product: "))
    cost = float(input("The cost of the product: $"))
    choice = str(input("Do you want to continue? [y/n]: "))
    total += cost
    if cost > 1000:
        cont_cost += 1
    if cost < cheapest or cont == 0:
        cheapest = cost
        cheapest_name = name
    cont += 1
    if choice not in ('y','yes'):
        break

print ('=-='*15)
if cont == 1:
    print (f'The total of the product is: {total}')
else:
    print (f'The total of the products is: {total}')
if cont_cost == 1:
    print (f'{cont_cost} product costs more than $1000')
elif cont_cost == 0:
    print (f'No product cost more than $1000')
else:
    print (f'{cont_cost} products costs more than $1000')

print(f'The name of the cheapest product is {cheapest_name}')