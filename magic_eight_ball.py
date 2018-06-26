import random

answers = ["It is certain" , "Outlook good" , "You may rely on it" , "Ask again later" , "Concentrate and ask again", "Reply hazy, try again" , "My reply is no" , "My sources say no"]

question = raw_input("Ask me anything: \n")
while question != "stop":
    print(random.choice(answers))
    question = raw_input("Ask me something else or tell me to stop: \n")
    if question == "stop":
        break
