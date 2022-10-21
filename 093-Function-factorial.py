'''Create a program that has a factorial() function that receives two parameters: 
the first that indicates the number to be calculated and the other called show, 
which will be a logical value (optional) indicating whether or not the process 
of calculating the factorial.'''

def factorial(num=0, show=False):
    """
    -> show de factorial of a number.
    :param num: number to be factored 
    :param show: option to show or not the calculation process
    :return: returns the factorial of "num"
    """
    f = 1
    for i in range(num,0,-1):
        f *= i
        if show == True:
            print(i, end='')
            if i >= 2:
                print(' x ', end='')
            else:
                print(' = ', end='')
    if show == False:
        print(f'{num} factorial is = ', end='')
    return f


n = int(input('Type an integer: '))
choice = str(input('Do you want to show the calculation process? (y/n): ')).lower()
if choice == 'y':
    show = True
else:
    show = False
print(factorial(n,show))
print('\33[32mGood bye...\33[m')
