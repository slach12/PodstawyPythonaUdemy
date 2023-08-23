cardList = [ "9", "9", "9", "9",
             "10", "10", "10", "10",
             "Jack", "Jack", "Jack", "Jack",
             "King", "King", "King", "King",
             "Queen", "Queen", "Queen", "Queen"
             "Ace", "Ace", "Ace", "Ace",
             "Joker", "Joker"
           ]


import random


def choose_random_numbers(amount, total_amount):
    numbers = []
    i = 0
    while i<amount:
        number =  random.randint(0,total_amount)
        if not number in numbers:
            numbers.append(number)
            i=i+1
    return numbers

def choose_random_numbers2(amount, total_amount):
    print(random.randint(0,total_amount))


def choose_random_numbers_with_sample(amount, total_amount):
    print(random.sample(range(total_amount),amount))




#choose_random_numbers2(6,49)

#print(choose_random_numbers(6,49))
#choose_random_numbers_with_sample(6,49)

'''
random.shuffle(cardList)
print(set(cardList))
print(random.sample( set(cardList) ,5))
'''

'''
random.shuffle(cardList)
print(cardList)
karta = cardList.pop()
print(karta)
'''

karty_gracza_1 = []
karty_gracza_2 = []
ile_kart = 5

random.shuffle(cardList)
for i in range(ile_kart):
    karty_gracza_1.append(cardList.pop())
    karty_gracza_2.append(cardList.pop())


print("Karty gracza 1 :",karty_gracza_1)
print("Karty gracza 2 :",karty_gracza_2)
