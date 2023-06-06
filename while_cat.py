#NB in python non esiste i++ come incrementatore, si usa i += 1(dove uno rappresenta di quanto incrementare)
i = 0
while i < 3:
    print("miaow")
    i += 1

#un altro modo per fare i loop e con ciclo for classi, ma in python eun po diverso
for e in [0, 1, 2]: #in python le liste si fanno cosi
    print("miaow2")

#un altro modo ancora e migliore e usare la function range:
for e in range(3):
    print("miaow3")

#e in python non hai bisogno di dichiarare la variabile su cui ciclare si li vuoi ciclare tutti senza prendere valore:
for _ in range(3):
    print("miao4")

#cosa ancora piu pythonica ma solo per conscenza non e carino da implementare
print("meows5\n" * 3, end="") #e otteniamo stesso risultato

##fatta come si deve diventa
def main():
    number = get_number()
    meaow(number)


def get_number():
    while True:
        n = int(input("What's is the number? "))
        if n > 0:
            return n


def meaow(n):
    for _  in range(n):
        print("meaow")


main()