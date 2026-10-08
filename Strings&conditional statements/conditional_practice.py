#Program to print yes when the age entered by the user is greater than or equal to 18
age = int(input("Enter your age:\n"))

if age > 18:
    print("Yes")
else:
    print("No")


#Program to find greatest of four numbers entered by the user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1 > num4):
    f1 = num1
else:
    f1 = num4

if(num2 > num1):
    f2 = num2
else:
    f2 = num1

if(f1>f2):
    print(str(f1) + " is greatest")

else:
    print(str(f2) + " is greatest")

