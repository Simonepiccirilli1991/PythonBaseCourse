import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit("Not enough command")
#la libreria request serve per fare chiamate verso servizi esterni
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

#la libreria json e compresa in python la uso per vedere meglio il json di risposta
#per predere il value devo fare response.json() se no prendo solo il valore dello status di risposta
print(json.dumps(response.json(), indent=2))