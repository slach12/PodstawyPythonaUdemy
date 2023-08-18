
'''
lista = ['A','B','C','D']

print(list)
print(enumerate(lista))


colors = ["red","green","blue"]
for i, color in enumerate(colors):
    print(i," : ",color)
    
'''


tasks = ["clean the kitchen","do laundry","pay bills"]

for i,task in enumerate(tasks,start = 1):
    task = task.capitalize()
    print(i,task)
