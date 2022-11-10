import pyperclip
import mysql.connector
import re
import subprocess

# problem with this line is continous prompt of password
# alternative is to run 'service mysql start' only at the beginning of accessing the mysql server
subprocess.run('/home/karma/CODE/python/Python_projects/multi-clipboard/service_start.sh')

mydb = mysql.connector.connect(host="localhost", user='root', passwd="password", database="copy")
storage = mydb.cursor()

commands = ["\n=== 'help' DOCUMENTATION ====\n", 'save <alias>', 'list', 'del <alias>/del all', 'help', "\n============ END =============\n"]
regex = {
    "save": re.compile(r'save( )(\w*)'),
    "del": re.compile(r'del( )(\w*)')
}
print('''
======== SAVE COPY ==========
''')
while True:
    command = input(">> ")
    
    # Help
    if command.lower() == 'help':
        for i in commands:
            print(i)
    
    # Exit
    elif command.lower() == 'exit':
        print("\n============ BYE =============")
        break
    
    # Save
    elif 'save' in command.lower():
        value = regex["save"].search(command)
        if not value:
            print("\n-- No Alias --\n")
        elif value.group(2) == '':
            print("\n-- No Alias --\n")
        else:
            storage.execute("insert into copy_list values(%s, %s)", (value.group(2), pyperclip.paste()))
            mydb.commit()
            print("\n  --saved--\n")
    
    # List
    elif command.lower() == "list":
        storage.execute("select * from copy_list")
        print()
        for i in storage:
            print(i[0])
        print()

    # Delete
    elif 'del' in command.lower():
        value = regex["del"].search(command)
        if not value:
            print("\n-- No Alias --\n")
        elif value.group(2) == '':
            print("\n-- No Alias --\n")
        
        # delete everything
        elif value.group(2).lower() == 'all':
            storage.execute('TRUNCATE TABLE copy_list')
            mydb.commit()
            print("\n  --CLEARED--\n")

        else:
            storage.execute('DELETE FROM copy_list WHERE id = "{}"'.format(value.group(2)))
            mydb.commit()
            print(f"\n  --{value.group(2).upper()} DELETED--\n")
    
    else:
        # retrive data/copy
        content = []
        storage.execute("SELECT * FROM copy_list")
        for i in storage:
            content.append(i[0])
        if command.lower() in content:
            storage.execute("SELECT content FROM copy_list WHERE id = '{}'".format(command.lower()))
            for i in storage:
                pyperclip.copy(i[0])
                print("\n  --RETRIEVED--\n")
        else:
            print("\n-- WRONG COMMAND/SYNTAX --\n")