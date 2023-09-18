import random


class Hat:
    #non usiamo init method perche questa classe non si istanzia . viene usata a mo di singleton
    house = ["Gryffindor, Slytherin", "Hafflepuff", "Ravenclaw"]#variabile di classe, accesibile alla classe

    @classmethod
    def sort(cls, name): #passiamo cls perche si riferisce alla classe e non a self istanza
        print(name, "is in", random.choice(cls.house))


Hat.sort("Harry") # per chiamare il metodo della classe mi riferisco al nome della classe stessa

