import random

options = {
    "rock": "123069",
    "paper": "45",
    "scissor": "78"
}
print('''==== ROCK PAPER & SCISSOR ====''')
while True:
    answer = input(">>> ").lower()
    value = str(random.randint(0,9))

    for i in options:
        if value in options[i]:
            print(i)
            if answer == i:
                print(" >>> It's a Draw <<<")
            elif answer == 'rock' and i == 'paper':
                print(" >>> You Lose <<")
            elif answer == 'paper' and i == 'scissor':
                print(" >>> You Lose <<")
            elif answer == 'scissor' and i == 'rock':
                print(" >>> You Lose <<")
            else:
                print(" >>> You Win <<")
    condition = input("AGAIN!!  (Y/N)?").lower()
    if condition == 'y':
        pass
    else:
        quit()