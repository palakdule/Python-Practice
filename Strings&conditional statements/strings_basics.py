#Concatinating two stings
greeting = "Good Afternoon, "
name = "Palak"

print(type(name))
c = greeting + name
print(c)

#indexing 
name = "Apurva"
print(name[4])
#name[3] = "d" --> does not work


#slicing 
print(name[0:3])

print(name[2:5])
print(name[:4]) #is same as name[0:4]
print(name[0:]) #is same as name[0:6]


#negative indices
print(name[-4:-1]) #is same as name[1:4]


#slicing with skip value
name = "PalakisGoddess"
d = name[0::4]
print(d)
