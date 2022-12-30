from Student import Student
from DataBase import load_db, save_db
from UserInterface import get_id, select, y_n
import UI_Teacher as t
import UI_Student as s


def main():
    data = load_db('data.json')
    students = [Student(**values) for values in data] if data else []
    search = {obj.surname: students_id for students_id, obj in enumerate(students)}
    while True:
        print("Начать работу?")
        if not y_n():
            break
        user = select()
        if user == 1:
            while True:
                action = t.input_action()
                if action == 4:
                    t.print_data(students)
                elif action == 3:
                    save_db('data.json', students)
                    break
                elif action == 2:
                    t.set_score(students[get_id(search)])
                else:  # action == 1:
                    students.append(t.add_student())
                    search[students[-1].surname] = len(students) - 1
        else:
            while True:
                action = s.input_action()
                if action == 1:
                    s.print_score(students[get_id(search)])
                else:  # action == 2:
                    break


if __name__ == "__main__":
    main()