'''develop a logic that reads a person's weight and height, calculates their BMI 
and displays their status, according to the table below:
- below 18.5: underweight
- between 18.5 and 25: ideal weight
- 25 to 30: overweight
- 30 to 40: morbid obesity'''

w = float(input("Your weight in kg: "))
h = float(input("Your height in meters: "))

bmi = w/(h**2)

if bmi < 18.5:
    print (f"Your BMI is {round(bmi,2)}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print (f"Your BMI is {round(bmi,2)}, you are in ideal weight.")
elif bmi >= 25 and bmi < 30:
    print (f"Your BMI is {round(bmi,2)}, you are over overweight.")
elif bmi >= 30 and bmi <= 40:
    print (f"Your BMI is {round(bmi,2)}, you are in morbid obesity.")