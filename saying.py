def main():
    hello("Jay")
    goodbye("Jack")

def hello(name):
    print(f"Hello {name}")

def goodbye(name):
    print(f"Goodbye {name}")
#viene usato per far partire il main quando si runna direttamente questa classe,
# in modo che se viene importata fara solo il metodo richiesto
if __name__ == "__main__":
    main()