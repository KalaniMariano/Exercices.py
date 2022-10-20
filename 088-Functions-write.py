'''Write a program that has a function called write(), 
which takes any text as a parameter and displays a 
message with an adaptable size.'''

def write(text):
    print('~'*(len(text)+4))
    print(f'  {text}  ')
    print('~'*(len(text)+4))

text = str(input('Write something: '))

write(text)