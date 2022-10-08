'''create a program that reads several integers from the keyboard. 
At the end of the run, show the average of all values ​​and what 
was the highest and lowest values ​​read. The program should ask 
the user whether or not he wants to continue typing values'''
choice = 0
cont_input = 0
sum_n = 0
n = 0
while choice not in ("no", "n"):
    n = int(input("Type a number: "))
    choice = str(input("Do you want to continue? yes or no: "))
    sum_n += n
    cont_input += 1

print (f"The average of the number is: {round((sum_n/cont_input),2)}")