import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")


def count_Task_Frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        #print(entry)
        if (entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]]+=1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1

    return completedTaskFrequencyByUser


def get_keys_with_top_value(my_dict):
    return [
        key
        for (key,value)in my_dict.items()
        if value == max(my_dict.values())
    ]

def users_with_top_completed_tasks(completedTaskFrequencyByUser):
    userIdWithMaxCompletedAmountOfTask =[]
    maxAMountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if(numberOfCompletedTask == maxAMountOfCompletedTask):
            userIdWithMaxCompletedAmountOfTask.append(userId)
    return userIdWithMaxCompletedAmountOfTask

#print(r.text)

#tasks = json.loads(r.text)
try:
    tasks = r.json()
except json.JSONDecodeError:
    print("Niepoprawny format")
else:
    #print("Wszystko jest ok.")
    #print(tasks[0])
    completedTaskFrequencyByUser = count_Task_Frequency(tasks)
    userWithTopCompletedTasks = users_with_top_completed_tasks(completedTaskFrequencyByUser)
#    print("Wręczamy ciasteczko mistrzunia do użytkowników o id:",userWithTopCompletedTasks)



#Sposób pierwszy
'''

r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()
#print(users)
for user in users:
    if user["id"] in userWithTopCompletedTasks:
        print("Wręczamy ciasteczko mistrzunia do użytkownika o imieniu :",user["name"])
        
''' 

#Sposób drugi
'''
print("Sposób drugii")

for userId in userWithTopCompletedTasks:
    #print(userId)
    #r = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users/",params = "id="+str(userId))
    user = r.json()
    #   print(user[0]["id"])
    print("Wręczamy ciasteczko mistrzunia do użytkownika o imieniu :",user[0]["name"])
'''

#Sposób trzeci

def change_list_into_conj_of_param(my_list, key="id"):
    conj_param = key + "="
    last_iteration = len(my_list)
    i=0
    for item in my_list:
        i+=1
        if(i == last_iteration):
            conj_param+=str(item) 
        else:
            conj_param+=str(item) + "&"+key+"="

    return conj_param

#conj_param=change_list_into_conj_of_param(userWithTopCompletedTasks)
conj_param=change_list_into_conj_of_param([2,4,7])
r = requests.get("https://jsonplaceholder.typicode.com/users/",params = conj_param)#+str(userId))
users = r.json()
for user in users:
    print("Wręczamy ciasteczko mistrzunia do użytkownika o imieniu :",user["name"])
