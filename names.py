name = input("Whats ur name? ")

file = open("names.txt", "a") #a sta per append, w per write se usi write riscrivi tutot i
# l file e cancelli i dati gia presenti
file.write(f"{name}\n")# metto \n perche voglio andare a capo, se no li mette tutti attaccati
file.close()

#per convenzione diventa
with open("names.txt", "a") as file:
    file.write(f"{name}\n")#in questo modo il close lo gestisce automatico

#per leggere
with open("names.txt","r") as file: #r sta per read
    lines = file.readlines() # questo metodo torna un lista con tutte le linee
for line in lines:
    print("Hello, ",line.rstrip())


# per convenzione lo facciamo diventare
with open("names.txt","r") as file: #r sta per read
    for line in file: #python in automatico prende tutte le linee del file anche senza specificare
        print("Hello, ",line.rstrip())

#per leggere dal file e riusare i valori
names = []
with open("names.txt") as file:# se non passiamo argomento di default e read
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")

# che puo diventare
with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, {line}")

# se volessimo settare piu valori come la casa di appartenenza possiamo usare un file .csv
# csv sta per comma separete value e separa i valori nella stessa riga usando ,(comma)
#percio supponiamo ci sia un file csv students.csv scritto cosi:
# Harry,Gryffindor
# Draco,Slytherin
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") #splitto dal comma e diventano una specie di array
        print(f"{row[0]} is in {row[1]}")

# in python si posso assegnare 2 o + variabili e un file che sara splittato
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") #siccome so gia che i valori sono 2, assegno a 2 variabili
        print(f"{name} is in {house}")

#ora se noi volessimo ordinarli per nome possiamo fare cosi
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {} #creo un dictionari dove assegnare chiavi e valori
        student["name"] = name
        student["house"] = house
        students.append(student)
        #tutto queste 3 righe posso farle diventare cosi
        student = {"name": name, "house": house}
        students.append()

def get_name(student):
    return student["name"]

#come chiave uso la funcion qui sopra che torna il nome dello studente, si puo fare in python
for student in sorted(students, key=get_name):#in python puoi fassare una funzione direttamente dentro un altra
    print(f"{student['name']} is in {student['house']}")

# anziche usare la get_name possiamo creare una lamba cosi:
for student in sorted(students, key=lambda student: student["name"]):#in python una lamba e cosi, stiamo passando i valori name come chiave
    print(f"{student['name']} is in {student['house']}")

#TODO: continua in names_pt2