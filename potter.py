name = input("What's ur name? ")

#questo e come lo switch case in java
match name:
    case "Harry":
        print("Gryffyndor")
    case "Hermione":
        print("Gryffyndor")
    case "Ron":
        print("Gryffyndor")
    #che diventa in python , posso concatenare cosi
    case "Ginni" | "Nevil" | "Cho":
        print("Gryffyndor")
    case "Draco":
        print("Slytherin")
    #questo e come il dafault value, qualsiasi cosa non sai nello switch va giu e l gestisce cosi
    case _:
        print("Who?")
