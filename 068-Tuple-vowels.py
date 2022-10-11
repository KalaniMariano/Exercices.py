'''create a program that has a tuple with multiple words (don't use accent). 
After that, you must show, for each word, which are its vowels.'''

words = ('pineapple','car','banana','orange','building','pudding','cellphone','pencil','computer','school','college')
print('Finding vowels: ')
for c in words:
    print (f'\nIn {c} we have: ', end='')
    for vowels in c:
        if vowels in "aeiou":
            print(vowels,end=' ')
            