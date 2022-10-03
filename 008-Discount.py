price = float(input("Price of the product: "))
while price <= 0:
    print ("The price must be greater than 0")
    price = float(input("Try again: "))
discount = float(input("How many % do you want to discount? "))
while discount < 0 or discount > 100:
    print ("The discount must be between 1 and 100%")
    discount = float(input("Try again: "))
x = (price/100)*discount
price = price - x
print ("The new price is: ", round(price,2))