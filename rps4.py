from random import random
import sys
import random
from enum import Enum
# sys.stdout.reconfigure(encoding='utf-8')
print("")

game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    
    print(' ')
    playerchoice = input("Enter...\n 1. for the Rock\n 2. for the paper\n 3. for the scissorrs\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("please choose the valid number that is 1 for rock 2 for paper and 3 for scissors")
        return play_rps()

    player = int(playerchoice)

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    print("") 

    print(f"You chose {str(RPS(player)).replace('RPS.', '')}.")
    print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.")
    print("")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "You win!!!"
        elif player == 2 and computer == 1:
            return "You win!!!"
        elif player == 3 and computer == 2:
            return "You win!!!"
        elif player == computer:
            return "Tie Game"
        else:
            return "Python Win"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    
    print("\n GameCount"  + str(game_count))



    while True:

        playagain = input("\nPlay Again? \nY for yes \nq to quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\nThank you for playing!")
        sys.exit()
        

play_rps()
