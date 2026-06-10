#dictionary
info = {
    "name" : "palak",
    "subjects" : ["python", "c", "java"],
    "topic" : ("dict", "set"),
    "learning" : "coding",
    "age" : 20,
    "is_adult" : True,
    "marks" : 94
}

print(info)
print(type(info))

print(info["name"])
print(info["subjects"])


#null_dict
null_dict = {}
null_dict["name"] = "palak"
print(null_dict)


#Nested Dictionaries
student = {
    "name" : "kunal",
    "subjects" : {
        "phy" : 92,
        "chem" : 94,
        "math" : 96
    }
}
print(student) #print subject
print(student["subjects"]) #print subjects
print(student["subjects"]["chem"]) #print chem marks


#Dictionary methods
#myDict.keys() {return all keys}
student = {
    "name" : "kunal",
    "subjects" : {
        "phy" : 92,
        "chem" : 94,
        "math" : 96
    }
}

print(student.keys())
print(list(student.keys())) #convert in list
print(len(student)) #print length of dict


#myDict.values() {return all values}

print(student.values())
print(list(student.values()))


#mydict.items() {return all key,val pairs as tuples}

print(student.items())
print(list(student.items()))

#myDict.get() {returns the key according to value}

#print(student["name2"]) #error
print(student.get("name2")) #no error = none

#myDict.update() {can insert items}

student.update({"city" : "delhi"})
print(student)
