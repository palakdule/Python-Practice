#set
collection = {1, 2, 3, 4, "hello", "world", 6}
print(len(collection))
print(type(collection))

#empty set
collection = set() #syntax

#set methods
#set.add()
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)


#set.remove()
collection.remove(1)
print(collection)


#set.clear()
collection.clear()
print(collection)
print(len(collection))


#set.pop() #pop ramdom values
collection = {"Hello", "palak", "world", "apple"}
print(collection.pop())


#set.union()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1)
print(set2)

#set.intersection()
print(set1.intersection(set2))


#sets
a = {1, 3, 4, 5, 1}
print(type(a))
print(a)


#This syntax will create an empty dictionary and not an empty set
b = {}
print(type(b))


#An empty set ca be created using the below syntax:
c = set()
print(type(c))
c.add(4)
c.add(5)
print(c)


#Set methods
#Creating am empty set
a = set()
print(type(a))

#Adding values to an empty set
a.add(4)
a.add(5)
a.add((4,5,6))
a.add(5) #Adding a value repeatedly does not changes a set
#a.add({4:5}) Cannot add list or dictionary to sets

print(a)

# Prints the length 
print(len(a)) 

# Removes 4 from set
a.remove(4)
# a.remove(44) #Throws and error (44 is not present in set)
print(a)


print(a.pop())
print(a)


a.clear()
print(a)

