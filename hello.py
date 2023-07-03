def main():
    x = input("What's ur name")
    print(hello(x))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()