# Program to store seven fuits in a list entered by the user
f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5: ")
f6 = input("Enter Fruit Number 6: ")
f7 = input("Enter Fruit Number 7: ")

myFruitList = [f1, f2, f3, f4, f5, f6, f7]
print(myFruitList)


# Program to accept marks of 6 students and display them in a sorted manner
m1 = int(input("Enter Marks for Student Number 1: "))
m2 = int(input("Enter Marks for Student Number 2: "))
m3 = int(input("Enter Marks for Student Number 3: "))
m4 = int(input("Enter Marks for Student Number 4: "))
m5 = int(input("Enter Marks for Student Number 5: "))
m6 = int(input("Enter Marks for Student Number 6: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)

#sum a list
a = [2, 4, 56, 7]

print(a[0] + a[1] + a[2] + a[3])
print(sum(a))



