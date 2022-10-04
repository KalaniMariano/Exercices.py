import random
import time

pc = 0
human = 0
options = ["PAPER","ROCK","SCISSORS"]

print ("PAPER-ROCK-SCISSORS GAME!")

games = int(input("How many games do you want to play? "))
if games == 0:
    print("Ok then, bye.")
    exit()
while games < 0: # Checking games input
    games = int(input("You can't play a negative number of games. Choose again: "))
print ("Ok lets go!\n")
time.sleep(1)
for i in range(games): # Number of games loop
    pcchoice = random.randrange(0,2) # PC choice
    print (f"Game {i+1}!")
    time.sleep(1)
    print ("Choose [1] for PAPER, [2] for ROCK and [3] for SCISSORS.")
    hchoice = int(input())
    hchoice -= 1
    while hchoice < 0 or hchoice > 2: # input verification
        hchoice = int(input("Try again: "))
    print (f"You choose {options[hchoice]}.")
    time.sleep(1.5)
    while pcchoice == hchoice:
        print (f"The computer choose {options[pcchoice]}!")
        time.sleep(1.7)
        print ("It is a draw!")
        print ("Go again. \n")
        time.sleep(1)
        print ("Choose [1] for PAPER, [2] for ROCK and [3] for SCISSORS.")
        hchoice = int(input())
        hchoice -= 1
        while hchoice < 0 and hchoice > 2:
            hchoice = int(input("Just options 1, 2 or 3"))
            hchoice -= 1
        print (f"You choose {options[hchoice]}.")
        pcchoice = random.randrange(0,2)
    if pcchoice == 0 and hchoice == 1:
        pc += 1
        print (f"The computer choose {options[pcchoice]}!")
        time.sleep(1.7)
        print (f"{options[pcchoice]} wins {options[hchoice]}")
        print (f"Computer scores {pc}!\n")
        time.sleep(1)
    elif pcchoice == 1 and hchoice == 0:
        human += 1
        print (f"The computer choose {options[pcchoice]}!")
        time.sleep(1.7)
        print (f"{options[hchoice]} wins {options[pcchoice]}")
        print (f"You scores {human}!\n")
        time.sleep(1)
    elif pcchoice == 2 and hchoice == 0:
        pc += 1
        print (f"The computer choose {options[pcchoice]}!")
        time.sleep(1.7)
        print (f"{options[pcchoice]} wins {options[hchoice]}")
        print (f"Computer scores {pc}!\n")
        time.sleep(1)
    elif pcchoice == 0 and hchoice == 2:
        human += 1
        print (f"The computer choose {options[pcchoice]}!")
        time.sleep(1.7)
        print (f"{options[hchoice]} wins {options[pcchoice]}")
        print (f"You scores {human}!\n")
        time.sleep(1)
    elif pcchoice == 1 and hchoice == 2:
        pc += 1
        print (f"The computer choose {options[pcchoice]}!")
        time.sleep(1.7)
        print (f"{options[pcchoice]} wins {options[hchoice]}")
        print (f"Computer scores {pc}!\n")
        time.sleep(1)
    elif pcchoice == 2 and hchoice == 1:
        human += 1
        print (f"The computer choose {options[pcchoice]}!")
        time.sleep(1.7)
        print (f"{options[hchoice]} wins {options[pcchoice]}")
        print (f"You scores {human}!\n")
        time.sleep(1)

print ("The game is finished!")
time.sleep(1)
print ("The final result is:")
print (f"You: {human}")
print (f"Computer: {pc}\n")
if human > pc:
    print ("You win!")
elif pc > human:
    print ("Computer wins :D")
else:
    print ("It was a draw!")
