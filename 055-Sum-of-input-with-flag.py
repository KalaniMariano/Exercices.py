'''create a program that reads several integers from the keyboard. 
the program will only stop when the user enters the value 999, 
which is the stop condition. At the end, show how many numbers 
were entered and what was the sum between them'''
print ("The program will stop if you type 999.")
n = 0
sum_n = 0
while n != 999:
    sum_n += n
    n = int(input("Type a number: "))
print (f"The sum of the numbers is: {sum_n}")