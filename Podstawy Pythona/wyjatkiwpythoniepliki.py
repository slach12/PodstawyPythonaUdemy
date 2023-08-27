

try:
    file = open("test.txt","w")
    file.write("sample")

    print(0/0)
    file.write("sample")
finally:
    file.close()
    a = 5
