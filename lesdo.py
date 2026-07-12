
import sys
def fizz():

    num = int(input("Please enter the number to check the fizz, Buzz or fizz Buzz =>\n"))

    if num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    elif num % 3 == 0 and num % 5==0:
        print("FizzBuzz")

    else:
        print(num)

        while True:

            playagain = input(f"\n do you wanna play again write yes to play and no to not play")

        if playagain.lower() == "yes":
                return fizz()

        elif playagain.lower() == "no":
            print("\n thank you for playing")
        else:
            print("please choose for yes or no")
            sys.exit

    fizz()