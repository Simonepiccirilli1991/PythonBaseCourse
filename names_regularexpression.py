import re

email = input("What's ur email ? ")

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

#che diventa
if re.search("^\w+@\w+\.edu$", email): #^ significa all'inizio della stringa, \w vuol dire che e accettata ogni parola compreso_,
    #@ divide l'oggetto email , \w uguale, ci deve essere una parola az 0-9 _ per essere accettata e \.edu$ vuol dire che deve finire con .edu la stringa dopo la @
    print("Valid")
else:
    print("Invalid")

#step up
if re.search("^\w+@(\w+\.)?\w+\.edu$", email, flags= re.IGNORECASE): #^ significa all'inizio della stringa, \w vuol dire che e accettata ogni parola compreso_,
    #@ divide l'oggetto email ,(\w+\.) indica any word + il. accettato nella parte dopo @, ? inidica che e opzionale, .edu$ indica che e obbligatorio finale
    print("Valid")
else:
    print("Invalid")