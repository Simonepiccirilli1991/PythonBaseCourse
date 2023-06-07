students = ["Harry", "Hermione", "Ron"]

for student in students:
    print(student)

#quello sopra diventa cosi in modo da tornare anche il numero
for i in range(len(students)):
    print(i + 1, students[i])

#Simile ad hasmap java, associa chiave valore,
students2 = {
    "Harry" : "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}
#in python se fai questo printi la chiave, in questo caso il nome, non il value associato
for student in students2:
    print(student , students2[student]) #per accedere al value va chiamato con la chiave in questo caso student stesso

#si evolve

students3 = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}

]

for student in students3:
    print(student["name"], student["house"], student["patronus"] , sep= ", ")