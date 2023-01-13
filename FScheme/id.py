#interactive dictionary
import json
from difflib import get_close_matches
with open('D:\projects/data.json') as f:
    data = json.load(f)
def translate(word):
    word = word.lower()
    if word in data:
        return data:
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("do you want to find %s" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes and n for no")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("wrong input! please enter y or n")
    else:
        print("wrong search!! please try again")
word = input("Enter the word you want to search")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)