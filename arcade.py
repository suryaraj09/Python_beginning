import argparse
from rps8 import rps
from guess_num import guess_game

def play_arcade(name):
    print("\n Welcome to the arcade! \n")
    print("\n Here are the games you can play:\n")
    playerchoice = input(f"which game do you want to play\n1. rock_paper_scissors\n2. guess_num\n")
    if playerchoice == "1":
        rps(name)
    elif playerchoice == "2":
        play = guess_game(name)
        play()
    else:
        print("\n Choose from the game above! \n")
        return play_arcade(name)

    while True:
        playagain = input(f"\n play again?, \n Type Y for yes \n Type Q to quit \n\n")
        if playagain.lower() not in ["y","q"]:
            print("Please choose from the parameters given above")
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_arcade(name)
    else:
        print("\nThank you for playing!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plays arcade games."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="the name of the player"
    )
    args = parser.parse_args()
    play_arcade(args.name)