# Andrew Batty
# 27/02/15
# Strecth and Challenge Task 1

import pickle

class birthday:
    def __init__(self):
        self.name = None
        self.dateOfBirth = None

child_name = input("Please enter the name which you would like to search for: ")

with open("birthday_file.dat", mode="rb") as birthday_file:
    birthdays = pickle.load(birthday_file)

if birthdays == child_name:
    print("This name is in the file.")
else:
    print("This name cannot be found in the file.")
    
