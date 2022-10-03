salary = float(input("Salary: "))
while salary <= 0:
    print ("The salary must be greater than 0")
    salary = float(input("Try again: "))
increase = float(input("How many % do you want to increase? "))
while increase < 0 or increase > 100:
    print ("The increase must be between 1 and 100%")
    increase = float(input("Try again: "))
x = (salary/100)*increase
salary += x
print ("The new salary is: ", round(salary,2))