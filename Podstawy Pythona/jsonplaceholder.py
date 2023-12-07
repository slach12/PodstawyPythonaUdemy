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
    print("Wręczamy ciasteczko mistrzunia do użytkowników o id:",userWithTopCompletedTasks)


r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()
#print(users)
for user in users:
    if user["id"] in userWithTopCompletedTasks:
        print("Wręczamy ciasteczko mistrzunia do użytkownika o imieniu :",user["name"])
        
    

 
