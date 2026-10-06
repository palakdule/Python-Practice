#List 
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])

#student list
student = ["Palak", 95.4, 17, "Delhi"]
print(student[0])
student[0] = "Kunal"
print(student)

#List Slicing (list_name[starting_idx : ending_idx])
marks = [85, 94, 76, 63, 48]
print(marks[:4])
print(marks[1:])

print(marks[-3:-1])

#List methods
#list.append() {adds one element at the end}
list = [2, 1, 3]
list.append(4)
print(list)

#list.sort() {sorts in ascending order}
list = [2, 1, 3]
print(list.append(4))
print(list.sort())
print(list)

#string example
list = ["banana", "apple", "mango"]
print(list.sort())
print(list)

#list.sort(reverse=True) {sorts in descending order}
list = [2, 1, 3]
print(list.append(4))
print(list.sort(reverse=True))
print(list)

#list.reverse {reverse list}
list = ['a', 'f', 'g', 'c', 'b']
list.reverse()
print(list)

#list.insert(idx, el) {insert element at index}
list = [1, 2, 3]
list.insert(1,5)
print(list)

#list.remove {remove first occurrence of element}
list = [2, 1, 3, 1]
list.remove(1)
print(list)

#list.pop(idx) {removes element at index}
list = [2, 1, 3, 1]
list.pop(2)
print(list)


#create a list using []
a = [1, 2, 4, 56, 88, 6]

#Print the list using print() function 
print(a)

#Access using index using a[0], a[1], a[2]
print(a[2])

#Change the value of list using 
a[0] = 98
print(a)

#we can create a list with items of different types
c = [45, "Palak", False, 4.9]
print(c)

#List slicing 
friends = ["Palak", "Apurva", "Deepika", "Rounak", 66]
print(friends[0:4])
print(friends[-4:])


#list methods
l1 = [1, 8, 7, 2, 21, 15]
print(l1)
# l1.sort() #sorts the list
# l1.reverse() #reverses the list
# l1.append(45) #adds at the end of the list
# l1.insert(3, 8) #inserts 8 at index 3
# l1.pop(2) #remove element at index 2
# l1.remove(21) #remove 21 from lists
print(l1)
