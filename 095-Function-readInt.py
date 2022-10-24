'''Create a program that has a function called readInt(), 
which will work similarly to Python's input() function, 
only validating to accept only a numeric value.
Ex: readInt('Enter an n')'''
def readInt(number):
    while True:
        print(number, end='')
        typed_number = str(input())
        if typed_number.isnumeric():
            return int(typed_number)
            break
        else:
            print("\033[031mOops, looks like you didn't typed an integer.\033[m")

n = readInt('Enter an integer: ')
print(f'You just typed the number {n}')
