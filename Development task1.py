# Andrew Batty
# 19/02/15
# Development Task 1

import pickle

class birthday:
    def __init__(self):
        self.name = None
        self.dateOfBirth = None

birthdays = []

person = birthday()
person.name = input("Please enter the name: ")
person.datOfBirth = input("Please enter the dat of birth: ")
birthdays.append(person)

with open("birthday_file.txt", mode="wb") as birthday_file:
    pickle.dump(birthdays,birthday_file)
    

