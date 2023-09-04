class Student:  #<- in py dentro le classi devi definire il costruttore come sotto, e si usa self di prassi oltre i vari parametri
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
# __str__ serve a fare il toString custom volendo, viene chiamata di defualt se vuoi prontare oggetto
    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():

    name = input("What's ur name ")
    house = input("What's ur house ")
    return Student(name, house)


if __name__ == "__main__":
    main()