#program to display a user entered name followed bt good afternoon using input() function
name = input("Enter your name\n")
print("Good Afternoon, " + name)


#program to fill in a letter template given with name and date
letter = '''Dear <|NAME|>,
You are selected!

Date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)


#program to detect double spaces in a string
st = "This is a string with double   spaces"
doubleSpaces = st.find("  ")
print(doubleSpaces)


#program to replace double spaces with single spaces
st = "This is a string with double  spaces"
st = st.replace("  ", " ")
print(st)


#program to format the following letter using escape sequence characters.
letter = "Dear Palak, This python course is nice! Thanks!"
print(letter)

formatted_letter = "Dear Palak,\nThis python course is nice!\nThanks!"
print(formatted_letter)
