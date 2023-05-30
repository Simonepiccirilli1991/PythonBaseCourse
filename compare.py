x = int(input("what's x? "))
y = int(input("what's y? "))

if x > y:
    print("x is higher than y")
elif x < y:
    print("x is lower than y")
else:
    print("x and y are equal")


## per concatenare le condizione negli if:
if x > y or x < y:
    print("x it not equal to y")