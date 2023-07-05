name = input("Whats ur name? ")

file = open("names.txt", "a") #a sta per append, w per write se usi write riscrivi tutot i
# l file e cancelli i dati gia presenti
file.write(f"{name}\n")# metto \n perche voglio andare a capo, se no li mette tutti attaccati
file.close()

#per convenzione diventa
with open("names.txt", "a") as file:
    file.write(f"{name}\n")#in questo modo il close lo gestisce automatico