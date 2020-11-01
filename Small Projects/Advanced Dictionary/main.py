# import All required modules
import json
from difflib import get_close_matches

# Main Body Code
data = json.load(open("data.json"))                             # Loading JSON File in the database

def defination(word):
    word = word.lower()
    got_it = get_close_matches(word, data.keys(), cutoff=0.8)
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(got_it) > 0:
        recieved = input("Did you mean %s Enter \"Y\" if yes otherwise \"N\": " % got_it[0]) 
        if recieved == "Y":
            return data[got_it[0]]
        elif recieved == "N":
            return "Word doesn't exist, please double check it."
        else:
            return "We didn't able to find such query."
    else:
        return "You have entered a wrong word. Please double check the it."

word = input("Enter a word: ")                                  # Getting User Input

output = defination(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(defination(word))