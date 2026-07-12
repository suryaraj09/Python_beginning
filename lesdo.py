import sys

def fizz():
    num = int(input("Please enter the number to check the fizz, Buzz or fizz Buzz =>\n"))

    
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

    while True:
        playagain = input("\nDo you want to play again? Write 'yes' to play and 'no' to exit: ").strip().lower()

        if playagain == "yes":
            return fizz() 
        elif playagain == "no":
            print("\nThank you for playing!")
            sys.exit()     
        else:
            print("Please choose 'yes' or 'no'")

fizz()
