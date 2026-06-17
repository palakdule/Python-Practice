#print element in a single line
fruits = ["mango", "banana", "apple", "grape"]

print(fruits[0], end=" ")

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(fruits)