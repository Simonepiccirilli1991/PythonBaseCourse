def main():
    name, house = get_student()
    print(f"{name} from {house}")
#in python puoi assegnare piu variabili sulla stessa riga in base al methodo che chiami e la tupla che torna
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name,house #in questo caso stiamo tornando una tuple, un unico oggetto con dentro 1 2 valori name e house

if __name__ == "__main__":
    main()