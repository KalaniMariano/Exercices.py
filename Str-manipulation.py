n = str(input("Type your full name: "))
print (f"Your name in lower case: {n.lower()}")
print (f"Your name in capital letters: {n.upper()}")
nsplit = n.split()
nsplit2 = ''.join(nsplit)
print (nsplit2)
print (f"Number of letters: {len(nsplit2)}")
print (f"Your first name has {len(nsplit[0])} letters")

