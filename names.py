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