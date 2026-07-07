import argparse
import random


def guess_game(name):
    game_count = 0
    player_wins = 0
    player_not_win = 0

    def play_guess_game():
        nonlocal game_count  
        nonlocal player_wins
        nonlocal player_not_win

        playerchoice = input(f"{name} Choose from the number 1 or 2 or 3 : ")

        if playerchoice not in ["1","2","3"]:
            print(f"please {name} choose from the above numbers only.")
            return play_guess_game()

        player = int(playerchoice)

        computer_choice = int(random.choice(["1","2","3"]))


        if player == computer_choice:
            print(f" {name} choice {player}")
            print(f" computer choice {computer_choice}")
            print(f"the number {name} guess was correct")
            player_wins += 1
        else:
            print(f" the number {name} choose {player} is not the same as computer choice {computer_choice}")
            print("try again!")
            player_not_win += 1

        game_count += 1
        print(f"game_count : {game_count}")
        print(f"{name}_wins : {player_wins}")
        print(f"player_not_win : {player_not_win}")

        while True:
            playagain = input(f"\n play again?, \n Type Y for yes \n Type Q to quit \n\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_game()
        else:
            print(f"\n Thank you for playing{name}!")

    return play_guess_game

            

    
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description = "this is a guessing number game"
    )

    PARSER.add_argument(
        "-n", "--name", metavar="name",
        required = True, help = "the name of the person to play the game with"
    )

    args = PARSER.parse_args()

    print(f"Hello {args.name}!\n")

    play = guess_game(args.name)
    play()