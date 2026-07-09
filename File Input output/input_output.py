#open file
f = open("demo.txt", "r")


#operation
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


#reading number of line
f = open("demo.txt", "r")

data = f.read(5)
print(data)

f.close()


#readline()
f = open("demo.txt", "r")

line1 = f.readline()
print(line1)

f.close()


#writing to a file
f = open("demo.txt", "w")
f.write("I want to learn python")
f.close()


#r+ mode
f = open("demo.txt", "r+")
f.write("abc")
print(f.read())
f.close()


#w+ mode
f = open("demo.txt", "r+")
print(f.read())
f.write("abc")
f.close()


#a+ mode
f = open("demo.txt", "a+")
print(f.read())
f.write("abc")
f.close()

#with Syntax
with open("demo.txt", "r")as f:
    data = f.read()
    print(data)

with open("demo.txt", "w")as f:
    f.write("new data")


#Deleting a file
import os
os.remove("sample.txt")
