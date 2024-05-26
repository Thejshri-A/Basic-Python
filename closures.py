def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins. ")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin. ")
        else:
            print("\n" + person + " has no coins left.")

    return play_game


tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()
tommy()
tommy()
jenny()
