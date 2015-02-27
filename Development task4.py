# Andrew Batty
# 19/02/15
# Development Task 4

import pickle

class birthday:
    def __init__(self):
        self.name = None
        self.dateOfBirth = None
        
with open("birthday_file.dat", mode="rb") as birthday_file:
    birthdays = pickle.load(birthday_file)
    
print("-"*17)
print("|{0:<6}|{1:<8}|".format("Name","DOB"))
print("-"*17)
for birthday in birthdays:
    print("|{0:<6}|{1:<8}|".format(birthday.name,birthday.dateOfBirth))
    print("-"*17)
