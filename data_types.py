import math

first = "Barack"
last = "Obama"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

decade = str(1910)  # stringify constructor
print("The data type of", decade, " is ", type(decade))

multiline = '''
Hey! How are you?

This is Barack Obama
'''

print(multiline)

# Escaping special characters
sentence = 'I\'m the line\tHey!\n\nSee slash\\now'
print(sentence)


# Some methods
print(first.lower())
print(first.upper())
print(multiline.title())  # It Shows Every First Letter Capitalised In Each Word
print(multiline.replace("Barack", "Michelle"))
print(multiline)

# Length
print("Actual length: ", len(multiline))
multiline += "                                   "
print("Length with space at end: ", len(multiline))
multiline = "                  " + multiline
print("Length with space at start: ", len(multiline))

# String methods to remove white space
print(len(multiline.strip()))
print(multiline.strip())
print(len(multiline.lstrip()))
print(multiline.lstrip())
print(len(multiline.rstrip()))
print(multiline.rstrip())

# Index values
print(first[1:-1])
print(first[0:])
print(first.startswith("B"))
print(first.endswith("B"))

# Boolean Values
my_value = True
x = bool(False)
print(type(x))
print(isinstance(my_value, bool))

# Complex Numbers
comp_val = 5+3j
print(type(comp_val))
print("Real Part: ", comp_val.real)
print("Imaginary Part: ", comp_val.imag)

# Built in functions for Numbers
gpa = 4.84
print("Absolute: ", abs(gpa))
print("Round: ", round(gpa))
print("Round to 1: ", round(gpa, 1))  # nearest decimal point

# Math Library
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting string value to integer value using int() constructor
zip_code = "600126"
zip_value = int(zip_code)
print(type(zip_value))
