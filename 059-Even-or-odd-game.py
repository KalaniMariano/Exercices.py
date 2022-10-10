'''make a program that plays even or odd with the computer. 
The game will only be stopped when the player loses, 
showing the total number of consecutive wins he achieved 
at the end of the game.'''
import random
prompt = "Choice [1]Even or [2]Odd: "
prompt2 = "Choose a number: "
n = 0
options = ["0", "EVEN", "ODD"]
pc_choice = 0
pc_choice_n = 0
result = 0
cont = 0
while True:
    while True:
        try: 
            choice = int(input(prompt))
        except:
            print ("Only numbers. Try again... ")
            continue
        if choice < 1 or choice > 2:
            print ("Just [1]Even or [2]Odd")
            prompt = "try again: "
        else:
            print (f"You choose {options[choice]}")
            if choice == 1:
                pc_choice = 2
                print (f"The computer is {options[pc_choice]}")
            else:
                pc_choice = 1
                print (f"The computer is {options[pc_choice]}")
            while True:
                try:
                    n = int(input(prompt2))
                except:
                    print ("Only numbers. Try again... ")
                    continue
                if n < 0:
                    print ("Just positive numbers!")
                    prompt2 = "try again: "                    
                else:
                    break        
            pc_choice_n = random.randint(0,1)
            result = (n + pc_choice_n) % 2
            print (f"The computer choose {pc_choice_n}")
            print (f"{n} + {pc_choice_n} = {n + pc_choice_n}")
            if choice == 1 and result == 0:
                print (f"{n + pc_choice_n} is even. You won!")
                print ("=-="*10)
                cont += 1
            elif choice == 1 and result == 1:
                print (f"{n + pc_choice_n} is odd. You lost!")
                print ("=-="*10)
                break
            elif choice == 2 and result == 1:
                print (f"{n + pc_choice_n} is odd. You won!")
                print ("=-="*10)
                cont += 1    
            else:
                print (f"{n + pc_choice_n} is even. You lost!")
                print ("=-="*10)
                break
    break
if cont == 1:
    print(f"You won {cont} time in a row.")
elif cont == 0:
    print ("You did't win a single time in a row.")
else:
    print(f"You won {cont} times in a row.")
print("Finished")
