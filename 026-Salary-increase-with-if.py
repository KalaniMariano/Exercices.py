salary = float(input("Enter a salary for increase: "))
while salary <= 0:
    print ("The salary must be greater than 0")
    salary = float(input("Try again: "))
if salary > 1250:
    x = (salary/100)*10
    salary += x
    print (f"The increase was 10%: R${round(salary,2)}")
else:
    x = (salary/100)*15
    salary += x
    print (f"The increase was 15%: R${round(salary,2)}")
