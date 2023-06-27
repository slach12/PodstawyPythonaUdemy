liczby = [1 ,2 ,3 , 4, 5,6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)


liczbyParzyste =[]
for element in liczby:
    if (element %2 == 0):
        liczbyParzyste.append(element)

print(potegiDwojki)
print(liczbyParzyste)

potegiDwojki2 = [ element**2
                  for element in range(20)
                  ]

print("potegiDwojki2")
print(potegiDwojki2)

liczbyParzyste2 = [ element
                    for element in liczby
                    if (element % 2 == 0)
                    ]

print("liczbyParzyste2")
print(liczbyParzyste2)


liczbyParzysteRazy3 = [ element*3
                        for element in liczby
                        if (element% 2 == 0 )
                        ]

print("liczbyParzysteRazy3")
print(liczbyParzysteRazy3)

liczbyPodzielne3Razy3 = [ element*3
                        for element in liczby
                        if (element% 3 == 0 )
                        ]

print("liczbyPodzielne3Razy3")
print(liczbyPodzielne3Razy3)

"""
[ co_zrobić_na_elemencie | for element in stara_lista | warunek_oparty_elemencie
"""
