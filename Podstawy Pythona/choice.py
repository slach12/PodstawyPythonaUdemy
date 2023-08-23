import random

movieList = ["Tytuł 1","Tytuł 2","Tytuł 3","Tytuł 4"]

event = ["śmierć","wygrana","przegrana","utrata złota","utrata życia"]
nagrodaZeSkrzynki = ["zielona","pomarańczowa","purpurowa","legendarna"]

#print(random.choice(movieList))
#print(random.choices(nagrodaZeSkrzynki,k=100))

from collections import Counter


print(Counter(random.choices(nagrodaZeSkrzynki,[80,15,4,1],k=1000)))

print(Counter(random.choices(nagrodaZeSkrzynki,[0.8,0.15,0.04,0.01],k=1000)))

