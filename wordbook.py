
import json
from difflib import get_close_matches


elements=json.load(open("wordbook.json"))
p=elements.keys()
def search_meaning(word):
    if word.lower() in p:
        return elements[word.lower()]
    elif word.upper() in p:
        return elements[word.upper()]
    elif word.title() in p:
        return elements[word.title()]
    elif len(get_close_matches(word,p))>0:
        closematch=get_close_matches(word,p)[0]
        user_decision=input("Are you looking for %s instead (Y/N)"%closematch)
        if user_decision=="y" or user_decision=="Y":
            return elements[closematch]
        elif user_decision=="n" or user_decision=="N":
            return "I can't find this word.Please look for spelling mistakes"
        else:
            return "I am sorry.I can not find your response"
    else:
        return "I can't find this word.Please look for spelling mistakes"



word=input("Enter searching key: ")
word=word.lower()
output=search_meaning(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)

exit()
