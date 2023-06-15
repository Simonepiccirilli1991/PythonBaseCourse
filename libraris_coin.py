import random #in questo modo sto importando tutta la libreria e tutti i metodi

coin = random.choice(["head", "tail"])
print(coin)

#cosi sto importando solo la funziona di cui ho bisogno
from random import choice

c = choice(["head","tails"])
print(c)

#cosi importo funzione da libreria e gli assegno un alias
from random import randint as roll

x = roll(1,10)
print(x)