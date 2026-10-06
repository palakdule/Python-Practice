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


# Creating tuple using ()
t = (1, 2, 4, 5)

# t1 = ()
t1 = (1,) # Tuple with single element 
print(t1)

#Printing elements of tuple using tuple
print(t[0])

# Cannot update the values of a tuple
t[0] = 34


# Tuple Methods
# Creating tuple Using ()

t = (1, 2, 4, 5, 4, 1, 2, 1 ,1)
print(t.count(1))
print(t.index(5))
print(t.index(5))
