import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("DictData.json"))

def translate(word):
    if word.isalpha() != True:
        return "This is not a word written using letters."
    else:
        word = word.lower()
        if word in data:
            output= data[word]
        elif len(get_close_matches(word, data.keys(), n=4)) > 0:
            trys = (get_close_matches(word, data.keys(), n=4))
            print("The best match is %s." % get_close_matches(word, data.keys())[0])
            print(data[get_close_matches(word, data.keys())[0]],"\n")

            for i in trys[1:]:
                    print(trys.index(i), " ", i)
            check =input("If you meant one of these words, type the number and hit enter.")
            try:
                print(trys[int(check)])
                print(data[trys[int(check)]])
            except:
                print("No choice number selected. Exiting.")
                exit()
        else:
            print("I don't recognize that word. Is it spelled right?")


word = input("Enter word: ")
translate(word)
