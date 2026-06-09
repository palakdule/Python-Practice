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
