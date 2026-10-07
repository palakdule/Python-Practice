#Program to create a dictionary of Hindi words with value as their english translation 
myDict = {
    "Pankha": "Fan",
    "Kitab": "Books",
    "Vastu": "Item"
}

print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
#print("The meaning of your word is:", myDict[a]) 
print("The meaning of your word is:", myDict.get(a))



#create an empty dictionary. allow 4 friends to enter their favorite language as values and use keys as their name 
favLang = {}
f1 = input("Enter your favorite language Palak\n")
f2 = input("Enter your favorite language Apurva\n")
f3 = input("Enter your favorite language Kittu\n")
f4 = input("Enter your favorite language sam\n")
favLang['Palak'] = f1
favLang['Apurva'] = f2
favLang['Kittu'] = f3
favLang['sam'] = f4

print(favLang)
