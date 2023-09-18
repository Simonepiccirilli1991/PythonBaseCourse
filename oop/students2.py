class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
     # __str__ serve a fare il toString custom volendo, viene chiamata di defualt se vuoi prontare oggetto

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls): # <- in questo modo tengo tutto dentro un la classe quello che riguarda la classe
        name = input("What's ur name? ")
        house = input("What's ur house ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()