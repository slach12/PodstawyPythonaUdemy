def pole_prostokata(a,b):
    return (a*b)

'''
print(5 * pole_prostokata(2,9))

pole_prostokataA = pole_prostokata(2,8)
pole_prostokataB = pole_prostokata(24,2)

print(5 * pole_prostokataA)
print(5 * pole_prostokataB)

print("Pole prostokąta = ", pole_prostokataA)
print(5*pole_prostokataB)
'''

def dzielenie(a,b):
    if (b == 0):
        return
    return a/b

print(dzielenie(10,0))
x=dzielenie(10,2)
if(x):
    print("Podzielono poprawnie ",x)
else:
    print("Coś poszło nie tak")
