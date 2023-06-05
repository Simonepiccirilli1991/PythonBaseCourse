def main():
    x = int(input("What's the number to check if it's even or prime"))
    if is_even2(x):
        print("even")
    else:
        print("is prime")


#Classica
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#nuova se po fa solo in python la prima, puoi mettere if , else e il return tutto su la stessia linea, la seconda e classica,
#torna per forza true o false gia de fault
def is_even2(n):
    #return True if n % 2 == 0 else False
    #ma mi basta mettere solo
    return n % 2 == 0

main()