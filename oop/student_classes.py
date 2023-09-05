class Student:  #<- in py dentro le classi devi definire il costruttore come sotto, e si usa self di prassi oltre i vari parametri
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
        self.patronus = patronus
# __str__ serve a fare il toString custom volendo, viene chiamata di defualt se vuoi prontare oggetto
    def __str__(self):
        return f"{self.name} from {self.house}"

    #getter, su getter si usa property come annotation
    @property
    def house(self):
        return self._house

    #setter
    @house.setter
    def house(self, house):#nel setter posso mettere logica
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    #metodo per far apparire emoji a seconda del patronus, mancano le emoji pero rende l'idea
    def charm(self):
        if self.patronus == "Stag":
            return "emoji1"
        elif self.patronus == "Otter":
            return "emoji2"
        elif self.patronus == "Jack Russell terrier":
            return "emoji3"
        else:
            return "emoji4"

def main():
    student = get_student()
    print(student)
    print(student.charm())


def get_student():

    name = input("What's ur name ")
    house = input("What's ur house ")
    patronus = input("What's ur patronus")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()