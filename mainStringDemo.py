
# ask user input
name = input("Write ur name").strip().title()

#in python se un valore si splitta, o ne ha piu di 1 in response puoi assegnare piu variabili in input
firstword, lastword = name.split(" ")

#Remove space
#name = name.strip()

#Uppercase 1st letter #Uppercare of every word
#name = name.capitalize()

#Uppercare of every word
#name = name.title()

#nuova feature, va messo f davanti il print line
print(f"Hello, {firstword}")
