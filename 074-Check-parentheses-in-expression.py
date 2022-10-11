'''Create a program where the user types any expression that uses parentheses. 
Your application should analyze whether the passed expression has the open 
and closed parentheses in the correct order.'''
expression = str(input('Type an expression [for example: ((a+b)*c)]: '))
count1 = expression.count('(')
count2 = expression.count(')')
count3 = expression.count('{')
count4 = expression.count('}')
count5 = expression.count('[')
count6 = expression.count(']')
if count1 == count2 and count3 == count4 and count5 == count6:
    print('Your expression is correct!')
else:
    print('your expression is wrong!')