def y_n() -> bool:
    while True:
        answer = input('(Y/N)?\n').lower()
        if answer == 'y' or answer == 'yes' or \
                answer == 'д' or answer == 'да':
            return True
        elif answer == 'n' or answer == 'no' or \
                answer == 'н' or answer == 'нет':
            return False
        print('Неверный ввод')


def get_id(search):
    while True:
        name = input("Введите фамилию: ")
        id = search.get(name, None)
        if id is not None:
            return id
        if name == "exit":
            exit(0)


def select():
    while True:
        print("| Учитель: 1 | "
              "Ученик: 2 |"
              )
        action = input("Введите действие: ")
        if action.isdigit() and action in ["1", "2"]:
            return int(action)