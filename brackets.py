# input 
s="()[){}()"

# answer
flag=0
#i=0

gen=(x for x in s)

print(len(s))

for i in range(round(len(s)/2)):
    
    item0 = next(gen)
    item1 = next(gen)
    #print(i+1)
    print(item0,item1)

    if (item0 == '(' and item1 == ')') or (item0 == '[' and item1 == ']') or (item0 == '{' and item1 == '}'):
        flag=1
    else: 
        flag=0
        break
    
if  len(s)%2==0 and flag==1:
    print(True)
else:
    print(False)


