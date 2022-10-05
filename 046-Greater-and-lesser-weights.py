'''make a program that reads the weight of five people. At the end, 
show which was the highest and which was the lowest weight read'''

print("Enter the weight of 5 people in kg.\n")

prompt = ""

high = 0
low = 0

for p in range(1,6):
    print (f"{p} > ", end='')
    while True:
        try:
            new= float(input(prompt))
        except:
            print("Only numbers, try again...")
            continue
        if new <= 0 or new >= 595:
            print("The weight must be between 0 and 595.")
            prompt = ""
        else:
            break
    if p == 1:
        high = new
        low = new
    else:
        if new > high:
            high = new
        if new < low:
            low = new

print (f"\nThe highest weight was {round(high,2)} and the lowest was {round(low,2)}")

    