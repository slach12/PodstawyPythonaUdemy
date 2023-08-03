def podwoj(x):
    return x*2

print(podwoj(2))

test = lambda x: x*2

print(test(2))


def funkcja_dla_przefiltruj(x):
    if (x % 2) == 0:
        return x
 
my_list = [2,14,22,7,6,4,5,17]

my_list_filtered = list(filter(lambda x: x%2==0 , my_list))

print(my_list_filtered)

my_list_filtered2 = list(filter(funkcja_dla_przefiltruj , my_list))

print(my_list_filtered2)


my_list_filtered3 = [x for x in my_list if (x % 2)==0]

print(my_list_filtered3)
