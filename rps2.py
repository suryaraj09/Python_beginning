from random import random
import sys
import random
from enum import Enum
# sys.stdout.reconfigure(encoding='utf-8')
print("")

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

playagain = True

while playagain:
    print(' ')
    playerchoice = input("Enter...\n 1. for the Rock\n 2. for the paper\n 3. for the scissorrs\n\n")

    if playerchoice not in ["1", "2", "3"]:
        sys.exit("please choose the valid number that is 1 for rock 2 for paper and 3 for scissors")

    player = int(playerchoice)

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    print("") 

    print(f"You chose {str(RPS(player)).replace('RPS.', '')}.")
    print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.")
    print("")

    if player == 1 and computer == 3:
        print("You win!!!")
    elif player == 2 and computer == 1:
        print("You win!!!")
    elif player == 3 and computer == 2:
        print("You win!!!")
    elif player == computer:
        print("Tie Game")
    else:
        print("Python Win")

    playagain = input("\nPlay Again? \nY for yes \nq to quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        playagain = False
        print("\nThank you for playing!")
        sys.exit()
