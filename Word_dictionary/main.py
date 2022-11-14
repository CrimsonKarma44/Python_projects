# import mysql.connector
import re

save = re.compile(r"(save) (\w*)")

dictionary = {}
def input_data():
    pass

print("====== DICTIONARY ======")
while True:
    word = input(">>> ")
    doc = save.findall(word)
    
    if save.search('save me'):
        print(True)
    else:
        print(False)
