A={1,2,3,4,5,5,6,1,2,3,5}

print(A)
A.add(12)
print(A)

AA = [1,4,20,-4,20]
BB = [2,1,25,20]
AA = set(AA)
BB = set(BB)

print(AA)
print(BB)

print('AA&BB')
print(AA&BB)

print('AA|BB')
print(AA|BB)

print('AA-BB')
print(AA-BB)

print('BB-AA')
print(BB-AA)

print('AA^BB')
print(AA^BB)


AA.discard(4)
print(AA)

print(AA.issubset(BB))
