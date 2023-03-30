# created by Lyka
# Date 27/02/2023
# Demonstarate asking the user a question
# provide a multiple choice answers,check if it's correct

name = input("State your name ")
print("Welcome" + name)

# This is a function called check(). It requires two arguments.
# One list and one user input.
# It returns True if the user input is in the list.
# It returns False if the user input is not on the list.


def check(options, user_input):
    if user_input in options:
        return True
    else:
        return False

options = ["7"]
question_one = input("How many continets are there? Is it: 7, 32, 9, 24?")
# print(check(options, question_one))
if check(options,question_one):
    print("Correct")
else:
    print("Incorrect")

options = ["mount everest"]
question_two = input("What is the highest mountain? Is it: Mount Fuji, Mount Cook, Mount Everest, Mount Kilimanjaro?").lower().strip()
# print(check(options, question_one))
if check(options,question_two):
    print("Correct")
else:
    print("Incorrect")

options = ["yes"]
question_three = input("Does Antartica count as a continent? Answer: No, Maybe, I don't know, Yes?").lower().strip()
# print(check(options, question_one))
if check(options,question_three):
    print("Correct")
else:
    print("Incorrect")

options = ["russia"]
question_four = input("What is the biggest country in the world? Answer: China, Russia, USA, Canda?").lower().strip()
# print(check(options, question_one))
if check(options,question_four):
    print("Correct")
else:
    print("Incorrect")

options = ["china"]
question_five = input("What country has the largest population in the world? Answer: China, Russia, USA, Canda?").lower().strip()
# print(check(options, question_one))
if check(options,question_five):
    print("Correct")
else:
    print("Incorrect")

options = ["nile river"]
question_six = input("What is the biggest river? Answer: Amazon River, Congo River, Nile River, Yellow River?").lower().strip()
# print(check(options, question_one))
if check(options,question_six):
    print("Correct")
else:
    print("Incorrect")

options = ["niue"]
question_seven = input("What is the smallest country based off population? Answer: Tuvalu, Niue, Marshall Islands, Monaco?").lower().strip()
# print(check(options, question_one))
if check(options,question_seven):
    print("Correct")
else:
    print("Incorrect")

options = ["sahara desert"]
question_eight = input("What is the largest desert? Answer: Gobi Desert, Sahara Desert, Thar Desert, there isn't one?").lower().strip()
# print(check(options, question_one))
if check(options,question_eight):
    print("Correct")
else:
    print("Incorrect")

options = ["north america"]
question_nine = input("What continent is Mexico in? Answer: Africa, Asia, North America, Europe?").lower().strip()
# print(check(options, question_one))
if check(options,question_nine):
    print("Correct")
else:
    print("Incorrect")

options = ["italy"]
question_ten = input("What country is Rome in? Answer: Italy, Frame, Romania, Spain?").lower().strip()
# print(check(options, question_one))
if check(options,question_ten):
    print("Correct")
else:
    print("Incorrect")

print("Thank you for playing the game")
