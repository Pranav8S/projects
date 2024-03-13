from itertools import combinations
import random

list_=[]

for i in range(5):
    list_.append(random.randint(-50,50))

print(list)

list_comb= list(combinations(list_,3))

print(list_comb)

dict_sum={}
values=[]

def largest(list_comb):
    
    for comb in list_comb:
        sum_=0

        for item in comb:
            sum_=sum_+item

        values.append(sum_)
        
        dict_sum.update({sum_:comb})

    return f"Largest comb-array is",dict_sum[max(values)],f"sum= {max(values)}"

print(largest(list_comb))

