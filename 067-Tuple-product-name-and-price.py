'''create a program that has a single tuple with 
product names and their respective resources, 
in sequence.
At the end, show a price listing, organizing 
the data in tabular form'''

info = ()
value = cont_product = product = 0
title = 'Product List'

while True:
    product = str(input("Product Name: "))
    info += (product, )
    value = float(input("Product Value: $"))
    info += (value, )
    option = str(input("Do you want to continue? [y/n]: "))
    if option in ('n'):
        break
print ('-'*40)
print (f'{title:^40}')
print ('-'*40)
for c in range (0,len(info),2):
    print (f'{info[c]:.<33}$', end='')
    print (f'{info[c+1]:>6}')