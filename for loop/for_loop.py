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
