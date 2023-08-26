
#import random

def transpose(olist):
    
    #print("==================================================================")

    tlist=[]
    
    #print(len(olist[0]))
    #print(len(olist))

    for i in range(len(olist[0])):
        inner_list=[]
        for j in range(len(olist)):
                inner_list.append(olist[j][i])
        tlist.append(inner_list)

    return tlist


# def main():

#     matrix2d=[]

#     for i in range(3):
#         inner_list=[]
#         for j in range(3):
#             inner_list.append(random.randint(10,99))
#         matrix2d.append(inner_list)

#     print(matrix2d)

#     t=transpose(matrix2d)

#     print(t)

# main()
