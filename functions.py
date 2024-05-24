def hello():
    print("Hello World!")


hello()

# Function to Sum


def sum1(num1=0, num2=0):  # Funtion has parameters
    print("The sum is : ", num1+num2)
    return num1+num2


# total = sum1(int(input("a: ")), int(input("b: ")))
# print("Total", total)

# Funtion to input multiple arguments


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items(1, 2, 3, 4)


def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_named_items(first="Dave", last="Grey")
