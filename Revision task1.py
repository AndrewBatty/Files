# Andrew Batty
# 19/02/15
# Revision Task 1


with open("my_file.txt", mode="w", encoding="utf-8") as my_file:
    for line in range(5):
        user_input = str(input("Please enter a line of text you wish to input into a text file: "))
        my_file.write(user_input)
