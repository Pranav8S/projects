# extract numbers from a string

str_="     4324 hellow there"

stack=[]

for i in str_.strip():
    if i.isdigit():
        stack.append(i)

print(stack)


s ="words and 987"
if s[0].isalpha():
    print(type(s[0]))

print("#"*154)
print("#"*154)






# collections module

import string
import random
from collections import Counter, namedtuple, defaultdict, deque


#counter
a=[]
for _ in range(50):
    a.append(random.choice(string.ascii_letters))

print(a)

print("#"*154)

print(Counter(a))



#named tuple
print("#"*154)

Point=(1,6)

print(Point)

Tuple = namedtuple('Point','x,y')

pt=Tuple(1,6)

print(pt)



#default_dict
print("#"*154)

d={1:2,3:4,7:8}

dd=defaultdict(float,d) # default value of int=0, float=0.0, str="", list=[]

print(dd[1])
print(dd[3])
print(dd[7])
print(dd[0]) 
print(dd[9])


#double ended queue
print("#"*154)

data=['a',6,True,9.67,'hig']

d=deque(data)


d.append(6)

d.appendleft(False)

print(d)

d.pop()

d.popleft()

d.extend([4,'hi',True])

# d.clear()

print(d)








print("#"*154)

from itertools import permutations, combinations, accumulate, groupby



a=[random.randint(1,39) for _ in range(3)]

b=[random.randint(1,39) for _ in range(3)]

print(a)

print(list(permutations(a,2)))

print(list(combinations(a,2)))

print("#"*154)


print(b)

print(list(permutations(b,2)))

print(list(combinations(b,2)))


# Combinations can be considered as unique permutations where the order doesn't matter.

# For example, in the context of our three letters A, B, and C:

# Permutations (order matters): AB and BA are considered distinct.
# Combinations (order doesn't matter): AB and BA are treated as the same combination.


print("#"*154)

add=accumulate(a)

print(list(add))  # logic similar to fibonaccai series


import operator

mul=accumulate(a, func=operator.mul)

print(list(mul))

max=accumulate(a, func=max)

print(list(max))


print("#"*154)

c=[random.randint(19,79) for _ in range(7)]

grp_obj= groupby(c,key=lambda x:x<50) # gives two list groped by - 1. less thaqn 50 and || 2. greater than 50

print(grp_obj)

for key, value in grp_obj:
    print(key, list(value))


print("#"*154)


l=(range(1,10))

print(l)

r=l[::-1]

print(r)