import random
from enum import Enum

Event = Enum('Event',['Chest','Empty'])

eventDictionary = {
                       Event.Chest: 0.6,
                       Event.Empty: 0.4

                   }

eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

Colours = Enum('Colours',{
                                'Green' : "zielony",
                                'Orange': "pomarańczowy",
                                'Purple': "fiolet",
                                'Gold'  : "złoty"
                                })


chestColoursDictionary = {
                            Colours.Green   : 0.75 ,
                            Colours.Orange  : 0.2 ,
                            Colours.Purple  : 0.04 ,
                            Colours.Gold    : 0.01
                         }

chestColoursList = tuple(chestColoursDictionary.keys())
chestColoursProbability = tuple(chestColoursDictionary.values())

rewardsForChests = {
                    chestColoursList[reward] : (reward + 1) * (reward+1)*1000
                    for reward in range(len(chestColoursList))
                    }

gameLength = 5
goldAcquired = 0

print("Welcome in my game called KOMNATA")
print("""You have only 5 steps to make,
    see yourself how much gold you gonna acquire till the end""")

while gameLength > 0 :
    gameAnswer = input("Do you want to move forward?")
    if ( gameAnswer == "yes"):
        print("Great, let's see what you got ...")
        drawnEvent = random.choices(eventList,eventProbability)[0]
        if (drawnEvent == Event.Chest ):
            print("You're drawn a CHEST")
            drawnColour = random.choices(chestColoursList,chestColoursProbability)[0]
            print("The chest colour is", drawnColour.value)
            gameReward = rewardsForChests[drawnColour]
            print("Nagroda",gameReward)
            goldAcquired  = goldAcquired + gameReward
        elif (drawnEvent == Event.Empty):
            print("You've drawn nothing, you are so unlucky!")
    else:
        print("You can go just straight man, nothing else, this game is d...")
        continue
    gameLength = gameLength - 1


print("Congratulation, you have acquired : ", goldAcquired)
   
    
