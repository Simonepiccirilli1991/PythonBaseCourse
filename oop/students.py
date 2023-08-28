def main():
    name, house = get_student()
    print(f"{name} from {house}")
#in python puoi assegnare piu variabili sulla stessa riga in base al methodo che chiami e la tupla che torna
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house #in questo caso stiamo tornando una tuple, un unico oggetto con dentro 1 2 valori name e house è immutabile
    # le parentesi nel return non sono obbligatorie le mettiamo per chiarezza

#possiamo refactorarla come segue:
def main2():
    student = get_student()
    print(f"{student[0]} from {student[1]}") # so gia il valore di ritorno della tupla, posso prenderli come una lista
if __name__ == "__main__":
    main()