import random

max_value= 0
sublist= []

def get_max_sublist(list_,sublist_len):

    if len(list_)<=sublist_len:
        return f"max_sublist= {list_}, sum= {sum(list_)}"
    
    else:
        
        for i in range(len(list_)-(sublist_len-1)):
            temp= list_[i:i+sublist_len]

            global max_value
            global sublist

            if max_value<sum(temp):
                max_value=sum(temp)
                sublist=temp
        
        return f"max_sublist= {sublist}, sum= {max_value}"



list_= [random.randint(-50,50) for i in range(10)]

print(list_)

print(get_max_sublist(list_,4))