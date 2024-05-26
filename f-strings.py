person = "Dave"
coins = 3

message = "\n %s has %s coins left." % (person, coins)
print(message)
message = "\n {} has {} coins left.".format(person, coins)
print(message)
message = "\n {1} has {0} coins left.".format(person, coins)
print(message)
message = "\n {person} has {coins} coins left.".format(
    person=person, coins=coins)
print(message)

player = {'person': 'Dave', 'coins': 3}
message = "\n {person} has dictionary {coins} coins left.".format(**player)
print(message)
message = f"\n {person.upper()} has f-string {coins} coins left."
print(message)
message = f"\n {player['person']} has f-string dictionary {coins} coins left."
print(message)

# Formatting options

num = 10
# Formatting options after the colon, here .4 represent upto 4 decimal values, and f stands for fixed
print(f"\n 2.25 times {num} is {2.25*num:.4f}")
for num in range(1, 11):
    print(f" 2.25 times {num} is :{2.25*num:.4%}")
