import unidecode

n = str(input("Type a phrase: "))
l = str(input("Which letter do you want information about? "))
u = unidecode.unidecode(n)
while len(l) == 0 or len(l) > 1:
    l = str(input("Choose just 1 letter: "))
print (f"Your sentence has {u.count(l)} letters '{l}'")
print (f"The letter appears first in position {u.find(l)+1} and the last time in position {u.rfind(l)+1}")
