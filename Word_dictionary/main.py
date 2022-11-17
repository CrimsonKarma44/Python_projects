import re

search = {
    'save': re.compile(r"(save) (\w+)"),
    'del': re.compile(r"(del) (\w+)"),
    'alt': re.compile(r"(alt) (\w+)")
}

storage = {}
def input_data():
    pass

print("====== DICTIONARY ======")
while True:
    word = input(">>> ").lower()
    delete = search["del"].search(word)
    save = search["save"].search(word)
    alt = search["alt"].search(word)

    if save:
        meaning = input("Meaning: ")
        storage[save.group(2)] = meaning
        if save.group(2) in storage.keys():
            print("======== SAVED =========")

    elif delete:
        storage.pop(delete.group(2))
        if delete.group(2) not in storage.keys():
            print("======= DELETED ========")

    elif alt:
        meaning = input("Meaning: ")
        storage[alt.group(2)] = meaning
        if meaning == storage[alt.group(2)]:
            print("======= ALTERED ========")
    elif word == 'dict':
        print("====== DICTIONARY ======")
        for x in storage.keys():
            print(x.upper() + ' => ' + storage[x])
            print()

    elif word in storage.keys():
        print(">>>", storage[word])

    elif word == 'exit':
        print("========= BYE ==========")
        quit()

    else:
        print("====== Wrong syntax =====")