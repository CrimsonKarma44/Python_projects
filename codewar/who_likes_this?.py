'''You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:'''


def likes(names):
    word, length, count = 'like this', len(names), 2
    if length == 1:
        return f"{names[0]} likes this"
    elif length == 2:
        return f"{names[0]} and {names[1]} {word}"
    elif length == 3:
        return f"{names[0]}, {names[1]} and {names[2]} {word}"
    elif length > 3:
        return f"{names[0]}, {names[1]} and {length-count} others {word}"
    return f'no one likes this'

love = likes(["David", "Peter", "dean", "Lily", "Seun"])
print(love)
love = likes([])
print(love)