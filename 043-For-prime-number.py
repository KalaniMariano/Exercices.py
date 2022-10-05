n = int(input("Type a number: "))
prime = 0
for i in range(1,10):
    if n % i == 0:
        prime += 1
print (prime)
if prime <= 2:
    print ("Prime")
else:
    print ("Not prime")
