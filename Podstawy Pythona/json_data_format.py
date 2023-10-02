import json

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

encodingFilm = json.dumps(film, ensure_ascii =False, indent = 4, sort_keys= True)

with open("sample.json", "w", encoding = "UTF-8") as file:
    json.dump(film,file, ensure_ascii = False)

'''
encodedRetrievedMovie = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decodedMovie = json.loads(encodedRetrievedMovie )


with open("sample.json",encoding="UTF-8") as file :
    wynik = json.load(file)

print("wynik")
print(wynik)
'''

print(encodingFilm)

with open("sample.json", encoding="UTF-8") as file:
    wynik = json.load(file)

print(wynik)


import  pprint

pprint.pprint(wynik)
