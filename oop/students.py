def main():
    name, house = get_student()
    print(f"{name} from {house}")
#in python puoi assegnare piu variabili sulla stessa riga in base al methodo che chiami e la tupla che torna
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house #in questo caso stiamo tornando una tuple, un unico oggetto con dentro 1 2 valori name e house è immutabile
#la tupla e immutabile nei valori che torna, non possono essere ovveridati , quindi se si vuole manipolare il dato va usata una lista
#possiamo refactorarla come segue:

def main2():
    student = get_student()
    print(f"{student[0]} from {student[1]}") # so gia il valore di ritorno della tupla, posso prenderli come una lista

## o possiamo usare un dictionari anziche tupla e diventa cosi :
def get_student_dic():
    name = input("what's name: ")
    house = input("what's house: ")
    return {"name": name, "house": house}


def main3():
    student = get_student_dic();
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}") #<- se usi " fuori devi usare ' dentro se no python impazzisce
#<--------------------------continua in student_classes.py ----------------->


if __name__ == "__main__":
    main()