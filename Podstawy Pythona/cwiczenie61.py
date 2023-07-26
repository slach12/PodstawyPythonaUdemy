def count(*arg):
    sum = 0
    for item in arg:
        sum= sum +item

    return sum


print(count(2,4,1,2,4,5,10))
