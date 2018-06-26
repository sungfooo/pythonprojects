import random

def ask_question():
    roll = raw_input("Do you want to roll? yes or no?")
    return roll

roll = raw_input("Do you want to roll? yes or no?")
while roll=="yes":
    print(random.randint(1, 6))
    roll = ask_question()
    if roll != "yes":
        break
