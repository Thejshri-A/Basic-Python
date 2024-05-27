from functools import reduce
def sum(a, b): return a+b


# sum = lamda a,b: a+ b
print(sum(4, 5))


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

############  Map  ################
numbers = [1, 2, 3, 4, 5]
squared_nums = map(lambda num: num*num, numbers)
print(list(squared_nums))
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(lambda acc, curr: acc+curr, numbers_list)
print(total)

names = ["Dave Gray", "Sarah Ita", "just another name", "yet another name"]
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
