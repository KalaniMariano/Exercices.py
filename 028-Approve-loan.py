print("You will enter the value of the house, a salary and how many years will the loan be repaid.")

house = float(input("House price: "))
salary = float(input("Salary: "))
years = int(input("Years to pay: "))

installment = house/(years*12)

if installment > salary * 0.3:
    print ("Loan denied. Amount of benefit greater than 30% of your salary.")
else:
    print (f"Loan accepted. The amount is {round(installment,2)} monthly")
