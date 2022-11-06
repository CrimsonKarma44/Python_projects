# time stamp 28:41


def main():
    print("Wwelcome to the emaail slicer")
    print()

    email_input = input("Input your emali address: ")

    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extensions: ", extension)

main()
