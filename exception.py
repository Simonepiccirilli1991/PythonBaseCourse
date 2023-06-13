try:
    x = int(input("What's x ? "))
    print(f"X values is {x}")
except ValueError:
    print("the input is not a integer")

#la best practies vuole che si faccia il try solo della funziona che puo crashare, quindi diventa come sotto
#in python  si puo usare else, per dirgli che se va tutto ok, fai questo. Altrimenti lui si stoppa
#in questo caso, se e un intero fa  tutto il giro, se va in ecceizione fa print dell'eccezione e si ferma
try:
    x = int(input("What's x ? "))
except ValueError:
    print("the input is not a integer")
else:
    print(f"X values is {x}")

#usando un while diventa cosi, in questo caso non si spacca a 26 perche se arriva arriva per forza con un valore
while True:
    try:
        x = int(input("What's x ? "))
    except ValueError:
        print("the input is not a integer")
    else:
        break

print(f"X values is {x}")

#piu completa usango una fuction
def main():
    x = get_int()
    print(f"X values is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x ? "))
        except ValueError:
            print("the input is not a integer")
            #pass e usato per non fare nulla, in casso di eccezzione

main()

