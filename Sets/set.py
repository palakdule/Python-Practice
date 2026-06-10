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
