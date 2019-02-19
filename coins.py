
no_count = 0
current_coins = 0

while no_count < 1:
    coins = True
    while coins:
        more_coins = input("You have %d coins. \nDo you want more? " % (current_coins,))
        if more_coins == "yes":
            current_coins = current_coins + 1
            break
        elif more_coins == "no":
            coins = False
            no_count = no_count + 1
        print("Bye")