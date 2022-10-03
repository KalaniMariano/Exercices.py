print ("Leap year or not...")
year = int(input("Type a year: "))

def leapyear(year):
    if year <= 1582:
        print (f"{year} was not a leap year.")
    elif year % 100 == 0:
        if year % 400 == 0:
            print ("Leap year.")
        else:
            print ("NOT leap year.")
    elif year % 4 == 0:
        print ("Leap year.")
    
leapyear(year)
