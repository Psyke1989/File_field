# My first try)))


import getpass

location = input("Where you use that Login and Password: ")
name = input("Input your login: ")
password = getpass.getpass(prompt='Password: ', stream=None)

print(f"Check corretly or not I remeber your login "
      f"and password. Location: {location}, Login: {name}, Password:{password}")

global agree
agree = input("'yes' or 'no': ")

if agree == "yes":
    with open("l_and_p.txt", "w") as d:
        print(f"Location: {location}", file=d)
        print(f"Login: {name}", file=d)
        print(f"Password: {password}", file=d)
    print("All recorded")


while agree != "yes":
    agree = input("'yes' or 'no': ")
    if agree == "yes":
        with open("l_and_p.txt", "w") as d:
            print(f"Location: {location}", file=d)
            print(f"Login: {name}", file=d)
            print(f"Password: {password}", file=d)
        print("All recorded")
    elif agree == "no":
        location = input("Where you use that Login and Password: ")
        name = input("Input your login: ")
        password = getpass.getpass(prompt='Password: ', stream=None)
        print(f"Check corretly or not I remeber your login "
              f"and password. Location: {location}, Login: {name}, Password:{password}")
    else:
        print("Type 'yes' or 'no' please. I not understand other words.")