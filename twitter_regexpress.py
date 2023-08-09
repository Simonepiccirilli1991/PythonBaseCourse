import re

url = input("Ur Url: ").strip()
#base , letteramente hardcodata
username = url.replace("https://twitter.com/", "")

usr = re.sub(r"^(https?://)?(www\.)?twitter\.com", "", url) #? vuol dire opzionale 0 o 1, \ e un escape epr indicare che il . e solo un .
#le parentesi servono a mettere tutto insieme
print(usr)

#final version
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))