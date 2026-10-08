#conditional
a = 45
if(a>3):
    print("The value of a is greater than 3")

elif(a>7):
    print("The value of a is greater than 7")

elif(a>13):
    print("The value of a is greater than 13")

elif(a>17):
    print("The value of a is greater than 17")

else:
    print("The value is not greater than 3 or 7")
print("Done")


# Multiple if statements
a = 45
if(a>3):
    print("The value of a is greater than 3")

if(a>7):
    print("The value of a is greater than 7")

if(a>13):
    print("The value of a is greater than 13")

if(a>17):
    print("The value of a is greater than 17")

else:
    print("The value is not greater than 3 or 7")
print("Done")



#is else optional?
a = 6
if(a==7):
    print("yes")
elif(a>56):
    print("no and yes")
else:
    print("I am optional")


#AND
age = int(input("Enter yout age: \n"))
if(age>34 and age<56):
    print("You can work with us")

else:
    print("You cannot work with us")


#OR
age = int(input("Enter yout age: \n"))
if(age>34 or age<56):
    print("You can work with us")

else:
    print("You cannot work with us")


#IS
a = None
if (a is None):
    print("Yes")
else:
    print("No")


#IN
a = [45, 56, 6]
print(45 in a)
print(78 in a)
