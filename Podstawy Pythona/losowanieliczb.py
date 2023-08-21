import random


'''
x = 0
while x <100:
    x=x+1
    print(random.random())
'''

x = 0
while x <100:
    x=x+1
    print(random.uniform(0,100))



def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChange = random.uniform(0,100)
    if (isHitChange <  weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"


print(will_weapon_hit(50))

x =0
listHit = []

while x <100:
    x = x+1
    listHit.append(will_weapon_hit(50))

print(listHit)
print('hit',listHit.count('hit'))
print('not hit',listHit.count('not hit'))

from collections import Counter

hitDiconary = Counter(listHit)
print(hitDiconary)


x = 0
while x < 20:
    x = x+1
    print(random.randrange(10))

x=0
while x < 20:
    x = x+1
    print(random.randint(0,10))    
