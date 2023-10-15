import math


### String Data type

# literal assignemt

first = 'Quduis '
last = 'Lateef'
fullname = first + last
print(fullname)


# Constructor assignement

fullname = str('Quduis Lateef')
print(fullname)

print("")

# Build a Menu
title = "menu".upper()
print(title.center(20, '='))
print("Coffee".ljust(16, ".") + "€4".rjust(4))
print("Muffins".ljust(16, ".") + "€12".rjust(4))
print("Cheesecake".ljust(16, ".") + "€6".rjust(4))

print("")

# String Index Values
print(first[1])  # second index value
print(first[-1])  # Last index value
print(first[1:-1])
print(first[1:])
print(first[:3])
print("")

# Some methods return Boolean data
print(first.startswith("Q"))
print(first.endswith("u"))

# Boolean Data types
myvalue = 'True'
z = bool(False)  # Using construction func
print(type(z))
print(myvalue)
print(isinstance(myvalue, bool))


# Numeric Data types
# INTEGER

num = 10
my_num = int(20)
print(type(num))
print(isinstance(my_num, int))

# FLOAT
gpa = 2.45
grade = float(3.5)
print(type(gpa))
print(isinstance(grade, float))

# COMPLEX
comp_value = 4 + 3j
comp_num = complex(7+8j)
print(type(comp_num))
print(comp_value.imag)
print(comp_value.real)

# Built-in Functions for numbers
print('')

print(abs(gpa))  # absolute values
print(abs(gpa * -1))  # print(abs(gpa) * -1) = -2.45
print(round(gpa))
print(round(gpa, 1))
# print(pow(9,-2))
# print(round(-2.5), round(-2.5, -1), type(gpa))
# print(max([6, 2]))
# print(min([6, 2]))
# print(sum([6, 2]))
# print(len(['a', 'b']))
# String Methods
print('\n')

#### Math method

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


# # String Methods
# name = "John Doe"
# lastName = name[-1]
# print(lastName)
# firstName = name[:-1]
# print(firstName)
# fullName = firstName + lastName
# print(fullName)
# print(name[::-1])
# print(name.upper())
# print(name.lower())
# print(name.replace("o", "-"))
# print(name.split(" ")[1])
# print('Hello' in name)
# print('Doe'.join(name))
# print(ord('H'))
# print(chr(72))
# print(format(int(time())))
# #List Methods
# fruits = ['apple', 'banana', 'cherry']
# numbers = [0, 1,2 ]
# print(fruits)
# print(numbers)
# print(sorted(fruits))
