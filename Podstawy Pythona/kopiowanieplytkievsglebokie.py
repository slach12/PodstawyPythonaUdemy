import copy

def evil_function(toBeDestroyedList):
    #toBeDestroyedList.List()
    #print("Przed")
    #print(id(toBeDestroyedList))
    #print(toBeDestroyedList)
    #print(id(toBeDestroyedList[0]))
    #toBeDestroyedList[0] = 11
    #print("Po")
    #print(id(toBeDestroyedList))
    #print(id(toBeDestroyedList[0]))
    #print(toBeDestroyedList)
    print(id(toBeDestroyedList))
    #toBeDestroyedList[0][0] = 20 
    print(toBeDestroyedList)
    
myList = [1,4,2,1,52,3]
#myList = [[1,4],[2,1],[52,3]]
print(id(myList))
print(myList)
evil_function((myList[:]))
print(myList)
