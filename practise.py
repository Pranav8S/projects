##################################basic i/o

"""print ("hello world")

print("  /|")
print(" / |")
print("/__|")

name="abcde"
age=29
if (age>18):
    isAdult= True
#print("hello "+name+" adult -" + isAdult)

phrase="hello tom this is earth v2"
print(phrase+" jjjj")
print(phrase.upper())

print(phrase.isupper())
print(phrase.upper().isupper())

print(len(phrase))

print(phrase[8])

print(phrase.index("m"))

print(phrase.replace("tom","jack"))


val=input("enter name ")
print("hi "+val)

num1=input("enter num1 ")
num2=input("enter num2 ")
result = num1+num2
print(result)
real_result=float(num1)+float(num2)
print(real_result)
"""



###################################lists

'''
books=[1, "kaevin" ,"idoh", False, 0x56]

print(books[2])
print(books[-3])

print(books[1:])
print(books[:-2])

print(books[:])

print(books[1:4])

books[3] = 1
books[0] = True
print(books)


friends=["Amy","George",4,False,0xf467f]

friends.extend(books)

print(friends)

friends.append(0x674)

print(friends)

friends.insert(2, "Jill")

print(friends)

friends.remove("George")

print(friends)

friends.pop()

print(friends)

print(friends.index(0xf467f)) 

friends.append(4)

print(friends.count(4))

print(friends.reverse())

print(friends)

friends2=friends.copy()

print(friends2)
'''

#########################################tuples

'''
coordinates=(1,5)

print(coordinates[1])
      
#coordinates[1]= "Jill"

list_of_coordinates=[coordinates,(7,9),(10,65)]

print(listofcoordinates)

print(listofcoordinates[:-2])

'''

""""
number_list=[1,2,3,4,5]

letter_list=["a","b","c","d","e"]

tuples_of_list=(number_list,letter_list,[True,False])

print(tuples_of_list)

del number_list[2:]

letter_list[4]="f"

print(tuples_of_list)

"""



#####################################dictionaries

'''
month = {"jan":"januray",
        "feb":"february",
        3:"march",
        "apr":"april",
    }

print(month["feb"])
print(month["apr"])

print(month.get("sep","key value pair not found"))
print(month.get(3))

month[7]="july"

month["apr"]="April"

print(month)

print(month[5])


'''


"""
cinfo = {"a":945764,
         "b":(5,"abc","0xf74",False),
        3:"abhsvs",
        "isLLL":True,
        99:"0x6537f",
        "fname":[{
            "Amy":"George",4:False,"abcccc":"0xf467f"}
            ],
        "numbers2":{0,2,4,6,8,4,2,0},
        }

print("")

print(cinfo)

print("")

print(cinfo["b"])

print("")

print(cinfo["b"][2])

print("")

print(cinfo["fname"])

print("")

for eachvalue in cinfo["fname"]:
    print(eachvalue[4])


"""

##############################set

"""

numbers1={1,3,5,7,9,9,9}
print(numbers1)
numbers2={0,2,4,6,8,4,2,0}
print(numbers2)

print("")
numbers3=numbers1.union(numbers2)

numbers3.update((10,))

print(numbers3)

numbers3.remove((10))

print(numbers3)

numbers4={1,4,7,10,5,10,11,56,35}

numbers5=numbers3.difference(numbers4)

print(numbers5)

"""



##########################################functions
'''
def say_hi(name,age):
    print("hello "+name+" "+age)
      
say_hi("mike","2")
say_hi("steve","6")


def cube(no):
    return no*no*no
    print("this wont print")

no =input("enter no ")
result = cube(int(no))

print(result)

'''


#######################################if-else

'''

is_male=False
is_tall=True

if is_male and is_tall:
    print("youre a male and youre tall")
elif is_male and not(is_tall):
    print("your a male but not tall")
elif not(is_male) and is_tall:
    print("youre not male but tall")
else:
    print("youre not a male and not tall")



def max_num(n1,n2,n3):
    if n1>n2 and n1>n3:
        print("n1 is max")
    elif n2>n1 and n2>n3:
        print("n2 is max")
    else:
        print("n3 is max") 

n1,n2,n3=int(input()), int(input()), int(input())
max_num(n1,n2,n3)

if "1" == 1:
    print("yes")

'''



###########################switch-case equivalent

"""
inp = input('enter language ')

match inp.lower():
    case 'python':
        print("python confirmed")
    case 'java':
        print("java confirmed")
    case _:
        print("enter either of python or java")


"""



###############################################while-loop

'''
i=0

while i<10:
    print(i)
    i=i+1

print("")

i=0
while i<5:
    j=0
    while j<=i:
        print("*",end="")
        j+=1
    print("")
    i+=1
'''


############################################for-loop

"""
for letter in "Hello World":
    print(letter)

print("")

friends=["jim", 1, 4, False, 0x481674]

for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])    

print("")

for i in range(7,10):
    print(i)

print("")

i=0
for i in range(5):
    j=0
    for j in range(0,i):
        print("*",end="")
    print("")
    i+=1

sum=1
num=float(input("enter no "))
val=int(input("enter exponent "))

if val>0:
    for i in range(val):
        sum=sum*num 
    print(sum)
else:
    print("enter positive val")

"""



########################################2d-array/nested-lists

'''
number_grid = [
    [1,2,3],
    ["a","b","c","d","e"],
    [True, False],
    [0x6574, "Jim"]
]

print(number_grid[3])
print(number_grid[1][2])

#print(number_grid.index("e"))

number_grid.extend(["JK0"])

name=["Jill", "Amy"]

number_grid.extend(name)

number_grid.append("0000")

print(number_grid)

number_grid.reverse()

print(number_grid)

del number_grid[:4]

#number_grid.remove("0000")

print(number_grid)

number_grid.pop()

print(number_grid)


matrix_grid=[
    [1,2,3],
    [4,5,6,7],
    [8,9],
    [0]
]

for row in matrix_grid:
    for col in row:
        print(col)

'''


####################################translator to convert vowel to 0

'''

def translate(phrase):
    
    vowels=["a","e","i","o","u"]
    
    for letter in phrase:
        if (letter.lower() in vowels):
            print(0,end="")
        else:
            print(letter,end="")    
        
#phrase = input("enter phrase ")
#translate(phrase)
'''



#################################exception-handling

"""
try:
    no = int(input("enter no "))
    value=no/0
    print(value)

except ZeroDivisionError as err:
    print(err)
    
except ValueError:
    print("invalid input!")

finally:
    print("this will print regardless of exception")
"""




######################################files

"""
emp_file=open("emp.txt","r")


print(emp_file.readable())
print("")
print(emp_file.readline())
print("")

#print(emp_file.readlines()[2])
print(emp_file.readlines())

print("")
print(emp_file.read())

emp_file.close()


emp_file=open("emp.txt","w")

emp_file.write("Kelly - Management")

emp_file.write("\nToby - HR")

emp_file.close()

emp_file=open("index.html","w")

emp_file.write("<p>this is HTML</p>")


emp_file.close()

"""



################lambda functions

#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

"""
def add_ten(a):
    a = a + 10
    print(a)

add_ten(5)


#the above function can be represented as below

add_ten = lambda a : a+10

print(add_ten(5))

print("")


mul_args = lambda a,b : a*b

print(mul_args(3,4))

"""



####################pass keyword

"""
def something():
    pass

class everything:
    pass

for i in range(5,100):
    pass

print("this will print ater skipping all above statements")

"""


#### list comprehention syntax

# new_list = [expression | for item in iterable | if condition]

# iterable has to be a list, tuple or a string


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [fruit for fruit in fruits if "a" in fruit]

print(newlist)



items=[1,3,5,7,9,11,13,15,17,19]

my_custom_list=[item**2 for item in items]

print(my_custom_list)

# in the above two examples the variable "fruit" and "item" can be replaced by "x"
# its just for iterating over each elment in the list


#simple even number list initialization
numerlist=[number for number in range(1,100) if number%2==0]

print(numerlist)

#2d to 1d matrix conversion (nested matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_1d=[item for sublist in matrix for item in sublist]

print(matrix_1d)


list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]

list3=[(x,y) for x in list1 for y in list2]

print(list3)

string_list="Hello bb@bbb World, vffg This is an zz$Zz example of filtering hlr0 using list && comprehention swp"

words=string_list.split()

vowels=["a","e","i","o","u"]

modified_string_list=[word for word in words if any(letter.lower() in vowels for letter in word)]

print(modified_string_list)





### decorators

import time

def get_time(func):
    def wrapper():
        t1=time.time()
        func()
        t2=time.time()-t1
        print(f"{func.__name__} took {t2} seconds")
    return wrapper    

@get_time
def func_a():
    print("this is function a")

@get_time
def func_b():
    print("this is function b")

func_a()
func_b()







###############practice your code below this line

"""
name = "sumanyu"
age="18"
print("my name is "+name+" and my age is "+age)

students=["pranav","sumanyu","srushti"]

students.append("hrishikesh")

print(students)

students.remove("sumanyu")

print(students)

students.insert(2,"sumanyu")

print(students)

"""


list_gen = (x for x in range(10))

print(list_gen)

#print(list(list_gen))

for item in list_gen:
    print(item)


result=float.is_integer(4)
