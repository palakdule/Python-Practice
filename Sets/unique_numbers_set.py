# Find unique numbers using a set

numbers = set()

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("\nUnique numbers:", numbers)
print("Total unique numbers:", len(numbers))
