def input_action():
    while True:
        print("| Узнат оценки: 1 | "
              "Выйти: 2 |"
              )
        action = input("Введите действие: ")
        if action.isdigit() and action in ["1", "2"]:
            return int(action)


def get_score(student):
    return student.subjects


def print_score(student):
    for subject, score in get_score(student).items():
        print(f"{subject}: {score}")