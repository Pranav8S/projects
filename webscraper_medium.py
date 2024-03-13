import requests
from bs4 import BeautifulSoup

url="https://medium.com/"

response = requests.get(url)

print(response)

html=response.text

soup=BeautifulSoup(html,"html.parser")

print(soup.title)

print("####################################################################")

#print(soup.prettify)

# print(soup.find_all("h4")[0].text)
# print(soup.find_all("h4")[1].text)
# print(soup.find_all("h4")[2].text)

#print("#################################################")

authors=[]
for index,author in enumerate(soup.find_all("h4")):
    # if author.text.strip() !="in":
    authors.append(author.text.strip())
    

#print(authors)

print("####################################################################")

#### stitching left middle and right value in the list where in is found
#### eg. 'Victor Timi', 'in', 'Level Up Coding' will be stitched to 'Victor Timi in Level Up Coding'

sources=[]

i=0
while i < len(authors):
    if authors[i]=="in":
        sources.remove(authors[i-1])
        source=authors[i-1]+" "+authors[i]+" "+authors[i+1]
        sources.append(source)
        i=i+2
    else:
        sources.append(authors[i])
        i=i+1

print(sources)
        

print("####################################################################")

headlines=[]
for index,headline in enumerate(soup.find_all("h2")):
    if index not in [0,1,8,len(soup.find_all("h2"))-1,len(soup.find_all("h2"))-2]:
        headlines.append(headline.text.strip())

print(headlines)

print("####################################################################")

# print(len(sources))

# print(len(headlines))

### making a dict from healines and sources list
if len(sources)==len(headlines):
    hs = zip(headlines,sources)
    dict=dict(hs)
print(dict)
