#while loop
count = 1
while count <= 5 :
    print("Hello")
    count += 1


i = 1
while i <= 99:
    print("ok", i)
    i += 1

#print from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

#print from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1

print("Loop ended")

#continue
i = 0
while i <= 5:
    if(i == 3):
        i+=1
        continue #skip
    print(i)
    i+=1
