#Program to print multiplication table of a given number using for loop
num = int(input("Enter the number: "))
for i in range(1,11):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}")


# Program to greet all the person names stored in a list l1 and which starts with S
l1 = ["Gobi", "Sam", "Sachin", "Saap"]
for name in l1:
    if name.startswith("S"):
        print("Hello " + name)


# Program to find whether a given number is prime or not
num = int(input("Enter the number: "))
prime = True
for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is prime")

else:
    print("This number is not prime")


#write a program to calculate the factorial of a given number using for loop
num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")


# Program to print the following star pattern
#   *
#  ***
# *****
n=3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))


#Program to print the following star pattern
# *
# **
# ***
n = 3
for i in range(3):
    print("*" * (i+1))


#Program to print multiplication table of n using for loop in reversed order
num = int(input("Enter the number: "))
for i in range(10,0,-1):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}")
