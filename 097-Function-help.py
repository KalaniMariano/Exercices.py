'''Make a mini-system that uses Python's interactive Help. 
The user will type the command and the manual will appear. 
When the user types the word 'END', the program will terminate.

NOTE: use colors.'''
def function_help(com):
    help(com)
def title(msg,color=0):
    size = len(msg)+6
    print('~'*size)
    print(f'   {msg}')
    print('~'*size)



while True:
    title('System of HELP Python.')
    command = str(input('Function or library ("END" to finish): '))
    if command.upper() in 'END':
        break
    else:
        function_help(command)
title('See you soon')