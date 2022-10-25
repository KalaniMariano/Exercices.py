'''Adapt the code from challenge 98, creating an additional function called 
currency() that can display the values ​​as a formatted currency value.'''

import coin

p = float(input('Type the price: $'))

print(f'The half of {coin.coin(p)} is {coin.coin(coin.half(p))}')
print(f'The double of {coin.coin(p)} is {coin.coin(coin.double(p))}')
print(f'Increasing 10% of {coin.coin(p)} we have {coin.coin(coin.increase(p,10))}')
print(f'Decreasing 13% of {coin.coin(p)} we have {coin.coin(coin.decrease(p,13))}')
