# Andrew Batty
# 19/02/15
# Development Task 3

import pickle

class birthday:
    def __init__(self):
        self.name = None
        self.dateOfBirth = None
        
with open("birthday_file.txt", mode="rb") as birthday_file:
    birthdays = pickle.load(birthday_file)

for birthday in birthdays:
        print(birthday.name,birthday.dateOfBirth)
