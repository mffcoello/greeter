import random

    greetings = [
        "Hello",
        "hi",
        "good morning",
        "HEY THERE!",
    ]

    name = raw_input("What is your name?")
        n = random.randint(0,3)
        print greeetings[n] + ", " + name + "!"
