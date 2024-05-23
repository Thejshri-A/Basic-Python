users = ["Dave", "John", "Sara"]

print("The list of users is : ", users)

users.append("Elisa")  # Using append method

users += ["Jason"]  # Using adding lists

users.extend(["Jimmy, Jackie"])  # Using extend method

data = [10, 50, 10]

users.extend(data)

users.insert(0, "Bob")

users[2:2] = ["Eddie", "Alex"]

users[1:3] = ["Robert", "Jay"]  # Replaces the value in the list

print("\n The new list after addition is : ", users)

# ------Remove Item from the List------

users.remove("Bob")

users.pop()
users.pop()
users.pop()

del users[2]

# del data
data.clear()
print("DATA", data)
print("\n The new list after removal is : ", users)

# ------Sorting the List------

users[1:2] = ['dave']
users.sort()
users.sort(key=str.lower)
print("\n The sorted List : ", users)

# ------Numbers in the list------

nums = [1, 5, 2, 7, 3]
nums.reverse()
# nums.sort(reverse=True)  # Descending order
print("\n This is a number list : ", nums)
print(" Descending Order: ", sorted(nums, reverse=True))

# ------Copy Methods------
numsCopy_1 = nums.copy()
numsCopy_2 = list(nums)
numsCopy_3 = nums[:]

print("Nums Copy : ", numsCopy_1, numsCopy_2, numsCopy_3)


# ------TUPLE------
my_tuple = tuple(("Dave", "Johnny", "Greece"))
another_tuple = (1, 2, 3, 4, 3, 3, 3)
print(my_tuple)
print(type(my_tuple))

# ------Tuples can not be modified------

my_list = list(my_tuple)
my_list.append("Eva")
new_tuple = tuple(my_list)
print("New Tuple : ", new_tuple)

# ------Unpacking a Tuple------
(one, two, *hey) = another_tuple  # everything remaining comes in *
print(one)
print(two)
print(hey)

# ------Tuple has two Methods only------
print(another_tuple.count(3))  # Counting the occurances of 3
print(another_tuple.index(3))  # Gives the index of occurances of 3
