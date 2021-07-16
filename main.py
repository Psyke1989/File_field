# My first try)))


import getpass

# блок отвечает за запрос и запись переменных вводимых пользователем
location = input("Where you use that Login and Password: ")
name = input("Input your login: ")
password = getpass.getpass(prompt='Password: ', stream=None)

# блок отвечает за уточнение правильности введённых данных пользователем
print(f"Check corretly or not I remeber your login "
      f"and password. Location: {location}, Login: {name}, Password:{password}")

# Необходимо для запуска цикла ниже
agree = str()

# Основной цикл с примитивным поведением при "да" или "нет".
# Если да, то происходит запись в файл.
# Если нет, то выполняется функция объявления переменных заново.
while agree.lower() != "yes":
    agree = input("'yes' or 'no': ")
    if agree.lower() == "yes":
        with open(f"{location}.txt", "w") as d:
            print(f"Location: {location}", file=d)
            print(f"Login: {name}", file=d)
            print(f"Password: {password}", file=d)
        print("All recorded")
    elif agree.lower() == "no":
        location = input("Where you use that Login and Password: ")
        name = input("Input your login: ")
        password = getpass.getpass(prompt='Password: ', stream=None)

        print(f"Check corretly or not I remeber your login "
              f"and password. Location: {location}, Login: {name}, Password:{password}")
    elif agree.lower() == "quit":
        break
    else:
        print("Type 'yes' or 'no' please."
              "I don't understand other words."
              "Or type 'quit' to exit from program.")

