class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("What's ur name ")
    student.house = input("What's ur house ")
    return student


if __name__ == "__main__":
    main()