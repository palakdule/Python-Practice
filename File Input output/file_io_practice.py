# Generate multiplication tables from 2 to 20

for i in range(2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}\n")


# Replace "Donkey" with a censored word

with open("sample1.txt") as f:
    content = f.read()

content = content.replace("Donkey", "######")

with open("sample1.txt", "w") as f:
    f.write(content)


# Censor a list of words

words = ["Donkey", "kaddu", "mota"]

with open("sample1.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "######")

with open("sample1.txt", "w") as f:
    f.write(content)


# Wipe out the contents of a file

filename = "sample1.txt"

with open(filename, "w") as f:
    f.write("")


# Rename a file

import os

oldname = "sample1.txt"
newname = "renamed_by_python.txt"

os.rename(oldname, newname)
