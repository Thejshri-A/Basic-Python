import os

# R - Read
# A - Append
# W - Write
# X - Create
f = open("E:\React\Apps\Python\File_Tutorial\gal_ames.txt")
# print(f.read(4))
print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("E:\React\Apps\Python\File_Tutorial\gal_ames.txt")
    print(f.read())
except:
    print("This file doesnot exist XD")
finally:
    f.close()

# Append - creates the file if the file doesn't exist
f = open("E:\React\Apps\Python\File_Tutorial\gal_ames.txt", "a")
f.write("\nNeil")
f.close()

f = open("E:\React\Apps\Python\File_Tutorial\gal_ames.txt")
print(f.read())

# Write
f = open("E:\React\Apps\Python\File_Tutorial\context.txt", "w")
f.write("I Deleted all of the contents")
f.close()

f = open("E:\React\Apps\Python\File_Tutorial\context.txt")
print(f.read())

# Two ways to create a file, if it does not exist
f = open("E:\React\Apps\Python\File_Tutorial\context_new.txt", "w")
f.close()

if not os.path.exists("E:\React\Apps\Python\File_Tutorial\context_create.txt"):
    f = open("E:\React\Apps\Python\File_Tutorial\context_create.txt", "x")
    f.close()

    # Delete the file
if os.path.exists("E:\React\Apps\Python\File_Tutorial\context_create.txt"):
    os.remove("E:\React\Apps\Python\File_Tutorial\context_create.txt")
else:
    print("File does not exist")

with open("E:\React\Apps\Python\File_Tutorial\gal_ames.txt") as fil:
    content = fil.read()
with open("E:\React\Apps\Python\File_Tutorial\context.txt", "w") as fil:
    fil.write(content)
