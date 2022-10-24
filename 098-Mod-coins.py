'''Create a module called coin.py that has built-in functions increase(), decrease(), double() and half().

Also write a program that imports this module and uses some of these functions.'''

import coin

p = float(input('Type the price: $'))

print(f'The half of ${p} is {coin.half(p)}')
print(f'The double of ${p} is {coin.double(p)}')
print(f'Increasing 10% of ${p}, we have {coin.increase(p,10)}')
print(f'Decreasing 13% of ${p}, we have {coin.decrease(p,13)}')