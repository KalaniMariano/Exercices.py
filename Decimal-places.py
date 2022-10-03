n = input("Type a number between 1 an 9999: ")
while len(n) > 4:
    n = input("Try again: ")
decimal = ["Thousand", "Hundred", "Ten", "Unity"]
for i in range (len(n)):
    print (f"{decimal[(i-len(n))]}: {n[i]}")
