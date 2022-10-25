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


def increase(n, v=0):
    """Increases a value by a specified percentage

    Args:
        n (float or int): value to be increased
        v (float or int, optional): value in percentage, increasing the number informed ('n'). Defaults to 100.

    Returns:
        float: returns the value increased by the specified percentage
    """
    increase_n = round((n/100)*v,2)
    n += increase_n
    return float(n)


def decrease(n, v=0):
    """Decrease a value by a specified percentage

    Args:
        n (float or int): value to be decreased
        v (float or int, optional): value in percentage, decreasing the number informed ('n'). Defaults to 100.

    Returns:
        float: returns the value decreased by the specified percentage
    """
    increase_n = round((n/100)*v,2)
    n -= increase_n
    return float(n)


def half(n):
    return n / 2


def double(n):
    return n * 2