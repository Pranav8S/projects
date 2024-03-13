import random

from random import choice

for i in range(10):
    result=choice(["Heads","Tails"])
    print(result)
    
print("")

for i in range(10):
    ans=random.randint(0,100)
    print(ans)

print("")

nolist=[]
for i in range(10):
    nolist.append(random.randint(0,100))

print(nolist)

random.shuffle(nolist)

print(nolist)

