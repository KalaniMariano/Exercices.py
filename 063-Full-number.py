'''create a program that has a fully filled tuple with a count in words from zero to twenty.
Your program should read a number from the keyboard (between 0 and 20) and display it in full.'''
full_number = ('ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN','TWENTY')
n = int(input('Type a number between 0 and 20: '))
while n < 0 or n > 20:
    n = int(input('Between 0 and 20: '))
print (f'{n} in full is: {full_number[n]}')