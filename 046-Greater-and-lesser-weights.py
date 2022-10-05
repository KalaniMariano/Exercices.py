'''make a program that reads the weight of five people. At the end, 
show which was the highest and which was the lowest weight read'''

print("Enter the weight of 5 people in kg.\n")

prompt = ""
highest_weight = 0
lowest_weight = 0
dif_highest_weight = 0
dif_lowest_weight = 0

for i in range(5):
    print (f"{i+1}> ", end="")
    while True:
        try:
            new_weight = float(input(prompt))
        except:
            print("Only numbers, try again...")
            continue
        if new_weight <= 0 or new_weight >= 595:
            print("The weight must be between 0 and 595.")
            prompt = "> "
        else:
            break
    if True:
        if lowest_weight == 0:
            lowest_weight = (new_weight - dif_highest_weight)
        elif new_weight > highest_weight:
            dif_highest_weight = new_weight - highest_weight
            highest_weight += dif_highest_weight
        elif new_weight < lowest_weight:
            dif_lowest_weight = lowest_weight - new_weight
            lowest_weight -= dif_lowest_weight

print (f"\nThe highest weight was {highest_weight} and the lowest was {round(lowest_weight,2)}")

    