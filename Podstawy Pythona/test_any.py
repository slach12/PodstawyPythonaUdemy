numbers1 = [1,3,5,6,7]
numbers2 = [1,3,5,7,9]
numbers3 = [2,4,6,8,10]

'''
def any_even(lista):
    for nr in lista:
        if nr % 2:
            return True
    return False

print(any_even(numbers1))
print(any_even(numbers2))

numbers1 = [ nr % 2 == 0 for nr in numbers1 ]
numbers2 = [ nr % 2 == 0 for nr in numbers2 ]

print(numbers1)
print(numbers2)

print(any(numbers1))
print(any(numbers2))
'''

def any_even(lista):
    return  any( [nr % 2 == 0 for nr in lista])


def all_even(lista):
    return  all( [nr % 2 == 0 for nr in lista])

print(any_even(numbers1))
print(any_even(numbers2))

if (any_even(numbers1)):
    print("Jest tu parzysta liczba")
else:
    print("NIE")


if (any_even(numbers2)):
    print("Jest tu parzysta liczba")
else:
    print("NIE")

print(all_even(numbers3))
