#2d matrix initialization

matrix2d=[]

for i in range(3):
    inner_list=[]
    for j in range(3):
        inner_list.append("*")
    matrix2d.append(inner_list)

print(matrix2d)

print("=========================================")
print("=========================================")
print("=========================================")




#3d matrix initialization


matrix3d=[]

for i in range(3):
    inner_list=[]
    for j in range(3):
        inner_most_list=[]
        for k in range(1):
            inner_most_list.append("#")
        inner_list.append(inner_most_list)
    matrix3d.append(inner_list)
    

print(matrix3d)