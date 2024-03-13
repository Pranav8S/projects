import re

file=open("regex_example.txt","r+")

data=file.read()
# words=re.findall(r'\w+',data)
file.close()

# x=re.search(r"\bab",data)
# print(words)

x=[]
y=[]
z=[]

for string in data.split():
    # print(word)
    if re.match(r".+@.+\..+",string):
        x.append(string)
    if re.match(r"^http",string):
        y.append(string)
    if re.match(r"\d",string):
        z.append(string)
    if re.match(r"^[A-Z].*[A-Z]$",string):
        print(string)
    if re.match(r"^a.*z$",string):
        print(string)
    
print(x,y,z)
    




