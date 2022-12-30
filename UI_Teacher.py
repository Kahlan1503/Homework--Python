from Student import Student


def add_student():
    name = input("Введите имя: ")
    surname = input("Введите Фамилию: ")
    group = input("Введите группу: ")
    return Student(name, surname, group)


def set_score(student):
    subject = input("Введите предмет: ")
    score = input("Введите оценку: ")
    student.add_score(subject, score)


def input_action():
    while True:
        print("| Добавить ученика: 1 | "
              "Добавить оценку: 2 | "
              "Сохранить базу и выйти: 3 | "
              "Вывести данные: 4 | "
              )
        action = input("Введите действие: ")
        if action.isdigit() and action in ["1", "2", "3", "4"]:
            return int(action)


def print_data(data):
    sep = max(len(str(i)) for i in data) * "-"
    print(sep)
    for value in data:
        print(value)
    print(sep)