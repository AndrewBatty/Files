# Andrew Batty
# 19/02/15
# Development Task 2

import pickle

class birthday:
    def __init__(self):
        self.name = None
        self.dateOfBirth = None

birthdays = []

for count in range(6):
    person = birthday()
    person.name = input("Please enter the name: ")
    person.dateOfBirth = input("Please enter the date of birth: ")
    birthdays.append(person)

with open("birthday_file.txt", mode="wb") as birthday_file:
    pickle.dump(birthdays,birthday_file)
    
