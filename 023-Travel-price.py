n = int(input("What is the distance of your trip in km? "))
while n <= 0:
    n = int(input("The distance must be grater than 0: "))
if n < 200:
    print (f"Your trip will cost: R${n/2}")
else:
    print(f"Your trip will cost: R${n*0.45}")