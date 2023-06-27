import sys
size =440

evenNumber = [element
              for element in range(size)
              if (element % 2 == 0)
              ]

evenNumberGenerator = (element
                       for element in range(size)
                       if (element % 3 == 0)
                       )
print("sum(evenNumberGenerator)")
print(sum(evenNumberGenerator))
print("sum(evenNumberGenerator)")
print(sum(evenNumberGenerator))

for item in evenNumberGenerator:
    print(item)

print("evenNumber")
print(sys.getsizeof(evenNumber))

print("evenNumberGenerator")
print(sys.getsizeof(evenNumberGenerator))


