'''Modify the functions that were created in challenge 98
so that they accept one more parameter, informing whether 
or not the value returned by them will be formatted by 
the currency() function, developed in challenge 99.'''

import coin

p = float(input('Type the price: $'))

print(f'The half of {coin.coin(p)} is {coin.half(p,True)}')
print(f'The double of {coin.coin(p)} is {coin.double(p,True)}')
print(f'Increasing 10% of {coin.coin(p)} we have {coin.increase(p,10,True)}')
print(f'Decreasing 13% of {coin.coin(p)} we have {coin.decrease(p,13,True)}')
