'''
yield - z ang. dostarczyć, dać , wydać z siebie

'''


def generate_even_numbers():
    for element in range(400):
        print("przed yield")
        if(element % 2 ) == 0:
            
            yield element
            print("po yield")
            

evenNumberGenerator = (element
                           for element in range(400)
                           if (element % 2 == 0 ))


a = generate_even_numbers()

print(a)
print(next(a))
print(next(a))


def generate_10_numbers():
    x = 0
    while x < 10:
        yield x
        x = x+1

print(list(generate_10_numbers()))
print(list(generate_10_numbers()))
print(list(generate_10_numbers()))

generate_10_numbers_expression = (x
                                  for x in range(10))


print(list(generate_10_numbers_expression))
print(list(generate_10_numbers_expression))
print(list(generate_10_numbers_expression))
