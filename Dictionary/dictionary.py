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


#Dictionary
myDict = {
    "Fast": "In a Qucik Manner",
    "Palak": "A Coder",
    "Marks": [1, 3, 6],
    "anotherdict": {'Palak': 'student'}
}

print(myDict['Fast'])
print(myDict['Palak'])
myDict['Marks'] = [34,77]
print(myDict['Marks'])
print(myDict['anotherdict']['Palak'])


#Dictionary methods
myDict = {
    "fast": "In a Qucik Manner",
    "palak": "A Coder",
    "marks": [1, 3, 6],
    "anotherdict": {'Palak': 'student'},
    1 : 2
}

print(myDict.keys())# Prints the keys of the dictionary
print(myDict.values()) # Prints the values of the dictionary
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 

updateDict = {
    "Apurva": "Friend"

}
myDict.update(updateDict) #update the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("palak")) # Prints value associated with key "palak"
print(myDict["palak"]) # Prints value associated with key "palak"

#Difference between .get and [] syntax in dictionaries
# print(myDict.get("palak2")) #Returns None as palak2 is not present i dictionary
# print(myDict["palak2"]) #throws an error as palak2 is not present in the dictionary
