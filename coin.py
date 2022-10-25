def readInt(number):
    """Checks if an input is an integer

    Args:
        number (any): input which will be checked

    Returns:
        int: if the input is numeric it will be returned as integer.
    """
    while True:
        print(number, end='')
        typed_number = str(input())
        if typed_number.isnumeric():
            return int(typed_number)
            break
        else:
            print("\033[031mOops, looks like you didn't typed an integer.\033[m")


def increase(n, v = 0,parameter = False):
    """Increases a value by a specified percentage

    Args:
        n (float or int): value to be increased
        v (float or int, optional): value in percentage, increasing the number informed ('n'). Defaults to 100.

    Returns:
        float: returns the value increased by the specified percentage
    """
    increase_n = round((n/100)*v,2)
    n += increase_n
    if parameter == True:
        return coin((float(round(n,2))))
    else:
        return float(round(n,2))


def decrease(n, v = 0, parameter = False):
    """Decrease a value by a specified percentage

    Args:
        n (float or int): value to be decreased
        v (float or int, optional): value in percentage, decreasing the number informed ('n'). Defaults to 100.

    Returns:
        float: returns the value decreased by the specified percentage
    """
    increase_n = round((n / 100)*v, 2)
    n -= increase_n
    if parameter == True:
        return coin((float(round(n, 2))))
    else:
        return float(round(n, 2))


def half(n, parameter = False):
    if parameter == True:
        return coin(round(n / 2, 2))
    else:
        return round(n / 2, 2)


def double(n, parameter = False):
    if parameter == True:
        return coin(round(n * 2, 2))
    else:
        return round(n * 2, 2)


def coin(n):
    n_str = str(n)
    size_n_str = len(n_str)
    rest = n - int(n)
    cont_size = comma = 0
    if n_str.count('.') == 1:
        if (round(rest*10,1)) - round(rest*10) != 0:
            size_n_str -= 3
            cont_size += 1
        else:
            size_n_str -= 2
   
    cont3 = 0
    list1 = []
    list1[:0] = n_str
    for i in range(1,size_n_str):
        if i % 3 == 0:
            cont3 += 1
            comma = size_n_str - cont3 * 3
            list1.insert(comma, ',')
    x = ''.join(list1)
    if cont_size > 0:
        return (f'${x}')
    else:
        return (f'${x}0')
    list1.clear()

