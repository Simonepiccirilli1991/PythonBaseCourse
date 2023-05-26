#python legge a cascatam quindi devo prima definire le funzioni e poi invocarle come a riga 11, altrimenti si spacca
def main():
    name = input("What's ur name?")
    hello(name)


def hello(name='no name'): #in questo modo gli stiamo dando un default value in caso ci arrivi oggetto vuoto
    print("Hello,", name)

#Cosi faccio partire la funzione, altrimenti nn  farebbe nulla
main()