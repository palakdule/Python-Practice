#tuple example
tup = (2, 1, 3, 1)
print(type(tup))

print(tup[0])
print(tup[1])

#create single tuple
tup = (1,)
print(tup)
print(type(tup))

#slicing
tup = (1, 2, 3, 4)
print(tup[1:3])

#Tuple methods

#tup.index {return index of first occurrence}
tup = (2, 1, 3, 1)
print(tup.index(2))

#tup.count {counts total occurrences}
tup = (2, 1, 3, 1)
print(tup.count(1))
