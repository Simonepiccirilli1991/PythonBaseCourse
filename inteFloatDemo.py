#int
x = input("what ur numeber")
y = input("what's ur second number")

#cosi printa stringa, ogni input viene considerato stringa
print(x+y)

#Cosi gli stiamo dicendo che sara un numbero e printera la somma in modo corretto
x = int(input("what's ur number ?"))
y = int(input("whatsUrNUmber"))

print(x + y)

#float prende i decimali
print("float time")
x = float(input("what's ur number ?"))
y = float(input("whatsUrNUmber"))

#rouad arrotonda al numero piu vicino a l'intero
z = round(x + y)
#qui stiamo dicendo di formattare e mettere la , dopo ogni decimale3
print(f"{z:,}")