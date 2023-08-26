import numpy as np
import random

"""

#1d array - simple list
a=np.array([1,3,5,7,9],dtype="int16")
print(a)

print(a.ndim," dimension")
print("shape =",a.shape)
print("data type=",a.dtype)
print("item size=",a.itemsize)
print("total size =",a.nbytes)

print("========================")

#2d array - list within a list
b=np.array([[9.6,8,6.2],
            [3.1,4.5,9],
            [2.6,7,3.4]])
print(b)

print(b.ndim," dimensions")
print("shape =",b.shape)
print("data type=",b.dtype)
print("item size=",b.itemsize)
print("total size =",b.nbytes)

print("========================")



#3d array - list within a list within a list
c=np.array([[[2,5],
            [1,8]],
             
            [[8,9],
            [6,7]],
              
            [[2,1],
            [0,8]],

            [[1,1],
            [9,9]]])
print(c)

print(c.ndim," dimensions")
print("shape =",c.shape)
print("data type=",c.dtype)
print("item size=",c.itemsize)
print("total size =",c.nbytes)

print("========================")

"""


#creating array
"""
a0=np.arange(7)
print(a0)

#array with step size
a1=np.arange(2,27,3)
print(a1)

#concatenation
print(np.concatenate((a0,a1)))

#empty array
o0=np.empty(3)
print(o0)

#array with fixed interval
lin_arr=np.linspace(0,100,num=5)
print(lin_arr)

print(np.linspace(2.0, 3.0, num=5))
      
print("========================")

#sort
rand_arr=np.random.randint(29,79,size=(3,3))
print(rand_arr)

print(np.sort(rand_arr))

print("========================")


print("========================")
arrx=np.random.randint(98,size=(2,3))
print(arrx)




#reshape
before=np.random.randint(89,size=90)
print(before)

after=before.reshape(9,10)
print(after)

print("========================")

reshaped_array=np.arange(15).reshape(3,5)
print(reshaped_array)

print("========================")

eg=np.array([[[1,7.7],[6.6,3]],
            [[2.2,5],[4,9.9]]])

print(eg)

print("3d array to 1d array",eg.reshape(-1))

print("========================")

print(np.linspace(15,85,num=35).reshape(5,7))

print("========================")
"""


###################access/modification


a= np.array([[1,3,5,7,9],
             [2,4,6,8,0],
             [1,6,9,4,4],
             [6,5,7,0,2]])
print(a.shape)
print(a)

print("========================")


"""

#[r , c] 
print(a[0,3])

print(a[-2,-3])

#only 4th column
print(a[:,3])

#only 2nd row
print(a[1,:])

print("========================")

#startindex:endindex:stepsize
print(a[:,1:4:1])
print("========================......")
print(a[:,1:-1:1])
print("========================")
print(a[0:-1:2,2])
print("========================")


a[2,3]=7
print(a)

print("========================")

a[:,2]=9
print(a)

print("========================")

a[1,:]=6
print(a)

print("========================")

a[1:3,2:4]=[[4,4],[5,5]]
print(a)

print("========================")

"""

b=np.array([[[1,7],[6,3]],
            [[2,5],[4,9]]])
print(b.shape)
print(b)

print("========================")

"""
print(b[0,1,1])

print("========================")

print(b[:,0,:])

print("========================")


b[:,1,1]=[1,1]
print(b)

print("========================")


c=np.array([[[1,7],
            [6,3]],
            [[2,5],
            [4,9]]])

d=b*c
print(c)

"""


"""
###################initialization of different arrays

#all 0's matrix
zeros=np.zeros((5,5))
print(zeros.shape)
print(zeros)

print("========================")

#all 1's matrix
ones=np.ones((3,3),dtype="int16")
print(ones.shape)
print(ones)

print("========================")

#any other nos
nine=np.full((2,2),999)
print(nine)

print("========================")

four=np.full_like(a,4)
five=np.full_like(b,7)

print(four)

print("========================")

print(five)

print("========================")


#random nos

randommatrix=np.random.randint(-8,77,size=(5,5))
print(randommatrix)

print("========================")

#identity matrix

id=np.identity(4)
print(id)

print("========================")

#repeat array

arr=np.array([1,2,3,4,5])
r_arr=np.repeat(arr,2)
print(r_arr)

print("========================")

m_arr=np.array([[1,2,3,4,5]])
rm_arr=np.repeat(m_arr,5,axis=0)
print(rm_arr)

print("========================")

arrr=np.ones((5,5))
print(arrr)

print("========================")

arrr[1:-1,1:-1]=0
arrr[2,2]=9
print(arrr)

print("========================")

#copy arrays

arr1=np.array([1,4,7,0])
arr2=arr1
print(arr2)
arr2[1]=9
print(arr2)
print(arr1)

print("========================")

arr2=arr1.copy()
arr2[2]=6
print(arr2)
print(arr1)

print("========================")



##################################mathematics



brr=np.array([1,3,5,7,9])
print(brr)

print("========================")
      
print(brr+-6)

print("========================")

print(brr*2)

print("========================")

print(brr/5)

print("========================")

print(brr**2)

print("========================") 


print("========================") 

#print(brr%2)

#print("========================") 

print(np.sin(brr))

print("========================") 

print(np.tan(brr))



#############################linear algebra


x= np.full((3,4),5)
print(x)

print("========================") 

y = np.ones((4,5))
print(y)

print("========================") 

#this wont work becuse of mismatch in sizes
#print(x*y) 

#the below will work because- n(columns-A)==no(coulmns-B)
print(np.matmul(x,y))

print("========================") 

#find determinant

#print(np.linalg.det(x))
print(np.linalg.det(ones))
print(np.linalg.det(id))
print(np.linalg.det(zeros))
#print(np.linalg.det(y))

print("========================") 

#inverse of matrix
x1=np.random.randint(0,99,size=(3,3))
y1=np.random.randint(29,49,size=(4,4))

print(np.linalg.inv(x1))

print("========================") 

print(np.linalg.inv(y1))

print("========================") 



#transpose of matrix
print(x1)
print("========================") 
print(np.transpose(x1))
print("========================") 
print(y1)
print("========================") 
print(np.transpose(y1))

print("========================") 


##########diagonal operations

a1=np.arange(-9,40,2)
print(a1)
print(a1.size)

a2=a1.reshape(5,5)
print(a2)

print("========================") 

print(np.diagonal(a2))
print("========================") 
print(np.triu(a2))
print("========================") 
print(np.tril(a2))
print("========================")
print(np.trace(a2))
print("========================") 



#################statistics


print("========================") 
print(a)
print("========================") 
print(b)
print("========================) 


print(f"min = {np.min(a, axis =1)}")

print(f"max = {np.max(a, axis=0)}")

print(f"25th percentile of a = {np.percentile(a,25,axis=0)}")

print(f"sum of b = {np.sum(b)}")

print(f"median of c = {np.median(b)}")

print(f"avg of c = {np.average(b)}")

print(f"std deviation of c = {np.std(b, axis=0)}")

print(f"variance of c = {np.var(b)}")



###############stack and split

print("========================")

v1=np.arange(0,7)

v2=np.full_like(v1,5)

v=np.vstack([v1,v2,v2,v1])

print(v)


v2=np.random.randint(49,size=(6,3))

print(v2)

print("========================+++++++")

print(np.vsplit(v2,3))

print("========================")



h1=np.ones((2,4))

h2=np.full((2,2),6)

h=np.hstack([h1,h2])

print(h)


h2=np.random.randint(49,size=(2,8))

print(h2)

print("========================")

print(np.hsplit(h2,4))

print("========================")



#########misc

datafile=open("datafile.txt","r+")

datafile.write("Below is a curated collection of educational resources, both for self-learning and teaching others, developed by NumPy contributors and vetted by the community. Theres a ton of information about NumPy out there. If you are just starting, wed strongly recommend the following:")

print(datafile.readable())

for line in datafile:
    print(line)

datafile.close()

print("========================")

filedata = np.genfromtxt("datafile.txt",delimiter=" ")

print(filedata)


numfile=open("numfile.txt","w+")

for i in range(150):
    numfile.write(str(random.randint(3,97))+" ")
    
print(numfile.readable())

with open("numfile.txt","r") as numfile:
    print(numfile.read())

numfile.close()

print("========================")

filedata = np.genfromtxt("numfile.txt",delimiter=" ")

print(filedata)

print("========================")

"""

##boolean masking and advanced indexing

d=np.array([1,3,5,7,9,2,4,6,8,0])

print(d)

print("========================")

print(d[0])
print(d[1])
print(d[6])
print(d[8])

#The above lines can be represented as:

print(d[[0,1,6,8]])

print("========================")

for i in d:
    if d[i]>4:
        print(d[i])

#the above line can be represented as below only the below one generates sorted list

print(d[d>4])
print("=============================")
print(d[d%2==0])
print("=============================")

f=(d[(d>2) & (d<8)])
print(f)

print(~((d>3) &  (d<8)))

print(np.any(d > 8))

print("=============================")

r=np.random.randint(77,size=(4,4))

print(r)

dim=(2,3)

print(r[dim])

r+=1
print(r)

#################

"""

arrl=np.random.randint(99,size=(6,5))

print(arrl)

print("====================================")

print(arrl[2:4,0:2])

print(arrl[[(0,1),(1,2),(2,3),(3,4)]])

print(arrl[[0,1,2,3],[1,2,3,4]])

print(arrl[[0,4,5],3:])


"""


