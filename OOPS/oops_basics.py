class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

# a = 12
# b = 34

# print("The sum of a and b is", a+b)
'''
PascalCase
EmployeeName --> PascalCase

camelCase
isNumeric, isFloatOrInt -->camelCase
'''


# Railway form example
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

palaksApplication = RailwayForm()
palaksApplication.name = "Palak"
palaksApplication.train = "Rajdhani Express"
palaksApplication.printData()


# Game example
class Remote():
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()
