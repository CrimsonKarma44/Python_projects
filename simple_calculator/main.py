def add(x, y):
    return int(x)+int(y)

def sub(x, y):
    return int(x)-int(y)

def mul(x, y):
    return int(x)*int(y)

def div(x, y):
    return int(x)/int(y)

print('== WHAT OPERATION WOULD YOU LIKE TO PERFORM ==')

while True:
    operation = input('>> ')
    if operation.lower() == 'add':
        x = input('x = ')
        y = input('y = ')
        print(add(x,y))
    elif operation.lower() == 'sub':
        x = input('x = ')
        y = input('y = ')
        print(sub(x,y))
    elif operation.lower() == 'mul':
        x = input('x = ')
        y = input('y = ')
        print(mul(x,y))
    elif operation.lower() == 'div':
        x = input('x = ')
        y = input('y = ')
        print(div(x,y))
    elif operation.lower() == 'exit':
        print("==================== BYE =====================")
        break
    else:
        print('Invalid operation')