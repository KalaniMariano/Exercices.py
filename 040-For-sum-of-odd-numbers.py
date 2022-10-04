#sum of all odd numbers that are multiples of 3 and that are in the range 1 to 500
s = 0
for i in range (1,500,2):
    if i % 3 == 0:
        s += i
print (s)