'''
numbers = (
    number
    for number in range(2,471)
    if (number % 7 ==0)

    )

for number in numbers:
    print(number)
'''

numbers = [
    number
    for number in range(2,471)
    if (number % 7 ==0)

    ]
print(numbers)


numbers_set = {
    number
    for number in range(2,471)
    if (number % 7 ==0)

    }
print(numbers_set)

