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
