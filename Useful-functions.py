def counter(i,f,p):
    from time import sleep
    print('=-='*20)
    if p == 0: #if step == 0
        p += 1 #add 1 to step

    if i > f and p > 0: #if the start is greater than the end and step is > 0, the step needs to be decreasing
        p *= -1         #so multiply the step by -1
    if i < f and p < 0: #same concept as the last "if"
        p *= -1         
    print(f'Count from {i} to {f}, from {p} to {p}')

    if p < 0:   #this "if" is for the "for" show the number that the user entered for the "end"
        f -= 1
    else:
        f += 1

    for x in range(i,f,p):
        print(x,end=' ')
        sleep(0.2)

    print('\33[32mTHE END...\33[m')


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


def readInt(number):
    while True:
        print(number, end='')
        typed_number = str(input())
        if typed_number.isnumeric():
            return int(typed_number)
            break
        else:
            print("\033[031mOops, looks like you didn't typed an integer.\033[m")


