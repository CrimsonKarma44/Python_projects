# ....Incomplete....


import random

def roll():
    return [random.randint(1,6), random.randint(1,6)]


dice = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }

while True:
    decision = input("Roll(Y/N)?").lower()
    if decision == "y":
        values = roll()
        print("you rolled {} and {}\n".format(values[0], values[-1]))
    elif decision == 'n':
        print("Thank you")
        break
    else:
        print("Wrong Syntax\n")