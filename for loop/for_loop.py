#for loop example
nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)


#ex
veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]

for val in veggies:
    print(val)

#tuple ex
tup = (1, 2, 3, 4, 2, 8, 9)
for num in tup:
    print(num)

#string ex
str ="PalakDule"
for char in str:
    print(char)

#break
str ="PalakDule"
for char in str:
    if(char == 'D'):
        print("D found")
        break
    print(char)


#For loop
fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
for item in fruits:
    print(item)


#for loop with else
#1
for i in range(10):
    print(i)
else:
    print("This is inside else of for")

#2
l = [1,7,8]
for item in l:
    print(item)
else:
    print("Done")

#Break statement
#1
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for") #This will not execute bcoz we use break in this program
#2
for i in range(0,80):
    print(i)
    if i == 3:
        break

#Continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

# Pass statement
#1
i = 4
if i>0:
    pass
while i>6:
    pass
print("Palak is Good girl")
#2
l = [1,7,8]
for item in l:
    pass
