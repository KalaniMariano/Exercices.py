'''create a program that calculates the amount to be paid for a product, considering its normal 
price and payment terms:
- cash/check: 10% discount
- cash on card: 5% discount
- up to 2x on the card: normal price
- 3x or more on the card: 20% interest'''

price = float(input("Price of the product: "))
payment = int(input("[1] for cash/check, [2] for card: "))
while payment < 1 or payment > 2:
    payment = int(input("Just options [1] or [2]!- "))
if payment == 1:
    x = price * 0.1
    price -= x
    print (f"We offer 10% discount in cash/check payment, the value of the product is now ${price}")
else:
    installment = int(input("How many times will you pay in installments on the card? "))
    if installment == 1:
        x = price * 0.05
        price -= x
        print (f"We offer 5% discount in cash payment on credit card, the value of the product is now ${price}")
    elif installment == 2:
        print (f"We don't offer discount for this type of payment, the value of the product is: ${price}")
        print (f"Getting ${price/installment} each installment")
    else:
        x = price * 0.2
        price += x
        print (f"The value of the product will have interest of 20%, the price is now ${price}")
        print (f"Getting ${price/installment} each installment")