# closure  is a function having access to the scope of it's parent function after the parent function has returned
# the closure is the nested function or the inner function

def parent_function(Person, coins):
    #coins = 3
    def play_games():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + Person + " "+"has" +" " +str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + Person + " "+"has" +" " +str(coins) + " coin left.")
        else:
            print("\n" + Person + " "+"has no"+" "+"coins left.")
    
    return play_games

tommy = parent_function("Tommy", coins = 3 )
jenny = parent_function("jenny" , coins = 6)

tommy()
tommy()
tommy()

jenny()
jenny()
jenny()
jenny()
jenny()
jenny()
