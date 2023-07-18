import re

email = input("What's ur email ? ")

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")