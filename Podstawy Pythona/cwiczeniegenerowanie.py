def number_multipled_by_itsefl_generator():
    number = 0;

    while True:
        number = number+1
        yield number*number

numberGenerator = number_multipled_by_itsefl_generator()

generateNumbers = []


for k in range(20):
    generateNumbers.append(next(numberGenerator))

print(generateNumbers)


#zamiast zmiennej k można użyć _
#k nic nie robi dlatego można opuścić

for _ in range(30):
    generateNumbers.append(next(numberGenerator))

print(generateNumbers)


#print(next(numberGenerator))
#print(next(numberGenerator))
#print(next(numberGenerator))
