import sys
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
# /home/deepaky/.PyCharmCE2019.3/config/scratches/main.py

print(type(data))

print(data["rain"])
print(data["acid rain"])
print(get_close_matches("rainn", data.keys(), n = 1))


def translate(w):
    close_by = get_close_matches(w, data.keys())[0]
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())):
        useryn = input(f"The word didnot exist, did you mean {close_by} instead? Enter yes or no: ").lower()
        if useryn == "yes":
            return data[close_by]
        elif useryn == "no":
            return "The word does not exists please check it again"
        else:
            return "Didnot understand the entry, please try again"
    else:
        return "The word does not exists please check it again"

word = input("Enter Word: ").lower()

output = translate(w=word)
print(type(output))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



