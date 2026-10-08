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


#Program to print yes when the age entered by the user is greater than or equal to 18
age = int(input("Enter your age:\n"))

if age >= 18:
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


#Program to find out wheather a student is pass or fail 
sub1 = int(input("Enter 1st subject marks:\n"))
sub2 = int(input("Enter 2nd subject marks:\n"))
sub3 = int(input("Enter 3rd subject marks:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congratulations! You passed the exam")


# A spam comment is definded as a text containing some keywords write a program to detect the spams
text = input("Enter the text\n")
spam = False

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")


#Program which finds out whether a given name is present in a list or not
names = ["palak", "apurva", "purva", "kittu", "bittu"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")

else:
    print("Your name is not present in the list")


#program to calculate the grade of a student from his marks from the given scheme
marks = int(input("Enter your marks\n"))
if marks>90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade = "F"

print("Your grade is " + grade)
