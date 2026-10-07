# Program to input eight numbers from the user and dislay all the unique numbers(once)
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
num6 = int(input("Enter number 6: "))
num7 = int(input("Enter number 7: "))
num8 = int(input("Enter number 8: "))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)


#can we have a set with 18(int) and "18"(str) as a values in it?
s = {18, "18"}
print(s)
print(len(s))


#What will be the length of following set
s = {20, 20.0, "20"}
print(s)
print(len(s))
