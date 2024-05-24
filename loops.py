value = 1

# ------While Loops------

# Basic While Loop
# while value <= 10:
#     print(value)
#     value += 1

# Break While Loop
# while value <= 10:
#     print(value)
#     if (value == 5):
#         break #if break the loop, then else will not execute
#     value += 1

# Continue While Loop
while value < 10:
    value += 1
    if (value == 5):
        continue  # Continues to the next iteration
    print(value)
else:
    print("Value is now equal to ", value)

# ------For Loops------
names = ["Dave", "Jessi", "Katie"]
for x in names:
    print(x)

for x in "Mississippi":
    print(x)

for x in range(2, 40, 5):
    print(x)
else:
    print("That's done!")


# Nested For Loops

names = ["Dave ", "Sara ", "John "]
actions = ["eats", "sleeps", "drinks"]

for name in names:
    for action in actions:
        print(name+action+".")
for action in actions:
    for name in names:
        print(name+action+".")
