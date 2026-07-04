person = "Dave"
coins = 3

# # print("\n" + person + "has" + str(coins) + "Coins left")

# message = "\n%s has %s coins left "  % (person, coins)
# print(message)
# message = "\n%s has %s coins left "  % (person, coins)
# print(message)




# message = "\n{} has {} coins left." .format(person, coins)
# print(message)

# message = "\n{1} has {0} coins left." .format(coins, person)
# print(message)

# message = "\n{person} has {coins} coins left." .format(coins = coins, person = person)
# print(message)

player = {'person' : 'Dave','coins' : 3}
# message = "\n{player.person} has {player.coins} coins left." .format(player = player)
message = "\n{person} has {coins} coins left." .format(**player)
print(message)              

#################
# f-strings! this is the way

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {coins * 2.5} coins left."
print(message) 

##############
# you can pass formatting options

num = 10
print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}")

num     =     10
print(f"\n{num * 2}")


player = {'person' : 'Dave','coins' : 3}

print(f"\n{player['person']} has {player['coins']} coins left.")