# Program to greet a user with "Good day" using functions
def greet(name):
    print("Good Day, "+ name)

greet("Palak")


#Program using function to find greatest of three numbers
def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(3, 5, 234)
print("The value of the maximum is " + str(m))


#Program using function to convert celsius to fahrenheit
def farh(cel):
    return (cel * (9/5)) + 32
c=34
f = farh(c)
print("Fahrenheit Temperature is " + str(f))


#How do you prevent a python print() function to print a new line at the end
print("Hello", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?")


#Write a recursive function to calculate the sum of first n natural numbers
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

n = int(input("Enter a number: "))
print(sum_n(n))


# Write a python function to print first n lines of following pattern
# ***
# **    n = 3
# *
def pattern(n):
    for i in range(n):
        print("*" * (n-i)) #print * n-i times
pattern(3)



num = int(input("Enter a number: "))
table(num)


#Write a python function to remove a given word from a string and strip it at the same time 
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Palak is a good girl     "
n = remove_and_split(this, "Palak")
print(n)


#Write a python function to print multiplication table of a given number 
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

num = int(input("Enter a number: "))
table(num)
