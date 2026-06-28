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

