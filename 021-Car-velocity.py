print ("This road has a radar of 80 km/h and the fine is R$7 for each km over the limit.\n")
v = int(input("What was the speed of the car when it passed the radar (Km/h)? "))
while v < 0 or v > 400:
    print ("It is not possible to reach the indicated speed on this road.")
    v = int(input("Try again: "))
if v > 80:
    print ("You were fined!")
    print (f"The fine is: R${(v - 80) *7}")
else:
    print ("You were not fined.")