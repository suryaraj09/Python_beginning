from random import random
import sys
import random
from enum import Enum
# sys.stdout.reconfigure(encoding='utf-8')
print("")

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0
    Tie = 0


    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal Tie

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

        print(f"You chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            nonlocal Tie
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win!!!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win!!!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win!!!"
            elif player == computer:
                Tie += 1
                return "Tie Game"
            else:
                python_wins += 1
                return "Python Win"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        
        print(f"\n GameCount  --> {str(game_count)}")
        print(f"\n Playerwins  --> {str(player_wins)}")
        print(f"\n Pythonwins  --> {str(python_wins)}")
        print(f"\n Ties  --> {str(Tie)}")



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

    return play_rps()
            

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()