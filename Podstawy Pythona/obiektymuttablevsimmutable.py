a = 4
print(a)
print('a.bit_count',a.bit_count())
print('a.conjugate',a.conjugate())
print('a.bit_length',a.bit_length())

listSample = [1,4,512, 24]
print('id(listSample)',id(listSample))
listSample2 = listSample
print('id(listSample2)',id(listSample2))
listSample2.append(465)
print('id(listSample2)',id(listSample2))
print('+++++++++++++')
print('listSample',listSample)
print('listSample2',listSample2)


print('id(listSample)',id(listSample))
print('id(listSample2)',id(listSample2))

a =4
print('a',a)
print('id(a)',id(a))
b = a
print('b',b)
print('id(a)',id(a))
print('id(b)',id(b))
b= 7
print('b',b)
print('id(b)',id(b))
print('a',a)

listSample2[1] = 1234
print('listSample',listSample)
print('listSample2',listSample2)


k= 4
h =4
print('id(k)',id(k))
print('id(h)',id(h))
h =25
print('id(h)',id(h))


c =5
print('id(c)',id(c))

def add(c, amount = 1):
    print('id(c)',id(c))
    c = c+ amount
    print('id(c)',id(c))

add(c)

def append_element_to_list(listka, element):
    print('id(listka)',id(listka))
    #listka.append(element)
    a = [1,2,3,4]
    listka = a
    print('id(listka)',id(listka))

print('id(listSample)',id(listSample))
append_element_to_list(listSample,55)
print('listSample',listSample)





