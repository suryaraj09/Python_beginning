from random import random
import sys
import random
from enum import Enum
print("")

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

playerchoice = input("Enter...\n 1. for the Rock\n 2. for the paper\n 3. for the scissorrs\n\n")

player = int(playerchoice)

if playerchoice < "1"  or playerchoice > "3":
    sys.exit("please choose the valid number that is 1 for rock 2 for paper and 3 for scissors")

computer_choice = random.choice("123")

computer = int(computer_choice)

print("") 

print("You choose" + ' ' + str(RPS(player)).replace('RPS.', '') + ".")
print("Python choose" + ' ' + str(RPS(computer)).replace('RPS.', '')  + ".")
print("")

if player == 1 and computer == 3:
    print("🥳You win!!!")
elif player == 2 and computer == 1:
    print("🥳You win!!!")
elif player == 3 and computer == 2:
    print("🥳You win!!!")
elif player == computer:
    print("🪢Tie Game")
else:
    print("🐍Python Win")
