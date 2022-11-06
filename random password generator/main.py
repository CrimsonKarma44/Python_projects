import string, random, re, pyperclip

character = list(string.ascii_letters + string.digits + '!@#$%^&*()')
digit = re.compile(r'[0-9]')

def generate_password(length):
    random.shuffle(character)
    password = ''
    for i in character[0:length]:
        password+=i
    if character[0] in '!@#$%^&*()' or character[0] in string.digits:
            generate_password(length)
    elif not digit.findall(password):
            generate_password(length)

    pyperclip.copy(password)
    return password


while True:
    print("Generate Password (Y/N)?")
    condition = input(">> ")
    if condition.upper() == 'Y':
        length = int(input("password length: "))
        if length == 0:
            print("Not fisible\n")
        else:
            password = generate_password(length)
            display_condition = input("Display password (y/n)? ")
            if display_condition == 'y':
                print(password, '\n')
    elif condition.upper() == 'N':
        print('Goodbye')
        break
    else:
        print("Wrong syntax\n")