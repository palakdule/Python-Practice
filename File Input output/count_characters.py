file = open("student.txt", "r")

data = file.read()

count = len(data)

print("Total characters:", count)

file.close()