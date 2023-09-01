class Student:  #<- in py dentro le classi devi definire il costruttore come sotto, e si usa self di prassi oltre i vari parametri
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():

    name = input("What's ur name ")
    house = input("What's ur house ")
    return Student(name, house)


if __name__ == "__main__":
    main()