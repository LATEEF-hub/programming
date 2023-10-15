##String Data type 

#literal assignemt 
first = 'Quduis '
last = 'Lateef'
fullname = first + last
print(fullname)


#Constructor assignement

fullname = str('Quduis Lateef')
print(fullname)

print("")

#Build a Menu
title = "menu".upper()
print(title.center(20, '='))
print("Coffee".ljust(16, ".") + "€4".rjust(4))
print("Muffins".ljust(16, ".") + "€12".rjust(4))
print("Cheesecake".ljust(16, ".") + "€6".rjust(4))

print("")

#String Index Values
print(first[1]) #second index value
print(first[-1]) #Last index value
print(first[1:-1])
print(first[1:]) 
print(first[:3])
print("")