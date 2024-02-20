def number_multipled_by_itsefl_generator():
    number = 0;
    while True:
        number = number + 1
        a = yield number * number
        number = a

generatedNumbers = []
numberGenerator = number_multipled_by_itsefl_generator()

numberGenerator.send(None)
#print(next(numberGenerator))
#numberGenerator.send(20)
#print(next(numberGenerator))

for i in range(20):
    generatedNumbers.append(numberGenerator.send(i))
print(generatedNumbers)

for i in range(30,50):
    generatedNumbers.append(numberGenerator.send(i))
print(generatedNumbers)
