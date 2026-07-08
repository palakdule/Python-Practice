#creating class
class Student:
    name = "Palak"


#creating object
s1 = Student()
print(s1.name)


#example
class Car:
    color = "blue"

car1 = Car()
print(car1.color)


#__init__ function
class Student:
    def __init__(self):
        print(self)
        print("adding new student in Database")

s1 = Student()
print(s1)


#example  
class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database")

s1 = Student("Palak")
print(s1.name)


#student 2
class Student:

    #default constructors
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database")

s1 = Student("Palak", 97)
print(s1.name, s1.marks)

s2 = Student("Binni", 88)
print(s2.name, s2.marks)


#class&instance attributes
class Student:
    college_name = "ABC College"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database")

s1 = Student("Palak", 97)
print(s1.name)


#Methods
class Student:
    college_name = "ABC College"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Palak", 97)
s1.welcome()
print(s1.get_marks())


#del keyword
class Student:
    def __init__(self, name):
       self.name = name

s1 = Student("Palak")
print(s1)
del s1
print(s1)


#private attribute and method
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account("12345", "abcde")

print(acc1.acc_no)


#example
class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
       self.__hello()

p1 = Person()
print(p1.welcome())

#Inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)


#multi-level inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()


#multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#super method
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("pirus", "electric")
print(car1.type)


#class method
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("Palak")
print(p1.name)
print(Person.name)


#example
class Person:
    name = "anonymous"

    @classmethod #decorator
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Palak")
print(p1.name)
print(Person.name)


#property decorator
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)


#Polymorphism
print(1 + 2)
print("chandu" + "chacha") #concatenate
print([1, 2, 3] + [4, 5, 6]) #merge

#complex example
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2): #dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()
