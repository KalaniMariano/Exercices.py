'''create a program that reads several integers from the keyboard. 
the program will only stop when the user enters the value 999, 
which is the stop condition. At the end, show how many numbers 
were entered and what was the sum between them. break'''
print ("The program will stop if you type 999.")
n = 0
sum_n = 0
while True:
    sum_n += n
    n = int(input("Type a number: "))
    if n == 999:
        break
print (f"The sum of the numbers is: {sum_n}")