band = {
    "name": "Rockstar",
    "instrument": "Viola"
}

band2 = dict(name="Bandstar", instrument="Guitar")

print(band)
print(band2)

# Accessing Items in dictionary
print(band["name"])
print(band.get("instrument"))

print(band.keys())  # List of Keys
print(band.values())  # List of values
print(band.items())  # List of key value pairs as tuples
print("Violin" in band)

# Change values in a dictionary
band["name"] = "Rockstars"
print(band)

# Added an item
band.update({"song": "cover"})
print(band)

# Remove an item
print(band.pop("name"))
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem())  # Returns a tuple, popping out the last term

# Delete an item
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print("Band 2 :", band2)

del band2

# Copy Dictionaries
band2 = band.copy()
band2["bass"] = "Dave"
print("Band : ", band)
print("Band2 : ", band2)

# Nested Dictionaries

member1 = {
    "name": "Dave",
    "instruments": "Guitar"
}
member2 = {
    "name": "Juke",
    "instruments": "Bass"
}
member3 = {
    "name": "Gren",
    "instruments": "Piano"
}

band3 = {
    "member one": member1,
    "member two": member2,
    "member three": member3,
}

print("Band 3 : ", band3)
print("Nested : ", band3["member one"]["name"])


# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4, 5))
print(nums2)
nums3 = {1, 2, 3, 4, 4, 5, 5, 6, 6, 6}
print("NUMS 3 No Duplicate", nums3)
nums.add(8)
morenums = {7, 9, 10}
nums.update(morenums)
print(nums)

# Merge Two Sets

a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9, 10}

newset = a.union(b)
print(newset)


# Keep only the Duplicate

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9, 10}

newset_dup = a.intersection(b)
print(newset_dup)


# Keep only the Duplicate

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

newset_sym_diff = a.symmetric_difference(b)
print(newset_sym_diff)
