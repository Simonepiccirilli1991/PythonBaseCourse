import sys

#prendo il secondo argomento perche il primo e in 0 dopo il comando per runnare python: ->  "python system_library.py Simone"
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("U don't have provided ur name")

## metodo 2 senza usare eccezzione, ma solo con logica
if len(sys.argv) < 2:
    print("Too few argoment")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
# se si passa argomento cosi python system_library.py "Simone Piccirilli"  <- tutto quello "" viene preso come un solo argomento

#altro modo usando sys.exit , una volta printato esce dal programma
if len(sys.argv) < 2:
    sys.exit("Too few argoment")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])