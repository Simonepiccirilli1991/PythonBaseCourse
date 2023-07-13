import csv

students = []
#Supponiamo che il file debba contenere delle , nel testo
# harry, "four mannor, main street" usando la libreria csv siamo in grado di leggerlo come segue:
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader: #se so quanti valore ha il file csv posso fare doppia variabile
        students.append({"name": name,"home": home}) #uso il dic per salvare oggetti in lista

for student in sorted(students, key=lambda student: student["home"]):
    print(f"{student['name']} is in {student['home']}")

#per rendere piu robusto  il tutto posso dichiarare le colonne e il relativo nome nel file csv:
# home, name
# wisley maison, ron
# posso accedere con un csv dictionari e diventa cosi:
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader: #usando il DictReader e avendo dichiarato il nome dei campi del csv a l'inizio del file fosso farlo
        students.append({"name": row["name"],"home": row["home"]}) #uso il dic per salvare oggetti in lista

for student in sorted(students, key=lambda student: student["home"]):
    print(f"{student['name']} is in {student['home']}")