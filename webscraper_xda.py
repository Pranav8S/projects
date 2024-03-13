import requests
from bs4 import BeautifulSoup

url="https://www.xda-developers.com/"

response = requests.get(url)

print("#################################################")

print(type(response))

html=response.text

print(type(html))

print("#################################################")
 
# if response.status_code == 200:
#     print(html)

soup=BeautifulSoup(response.text,"html.parser")

print(soup.title)

web_dl=open("newfile.txt","a")

if soup != None:
    web_dl.write(soup.prettify())

web_dl.close()

print("#################################################")

headlines=[]

print(soup.find_all("h3")[0].text) 
print(soup.find_all("h5")[0].text) 

print("#################################################")

for index,h3_element in enumerate(soup.find_all("h3")):
    headline = h3_element.text.strip()
    #print(headline)
    headlines.append(headline)
    if index==4:
        break


for h5_element in soup.find_all("h5"):
    headline = h5_element.text.strip()
    #print(headline)
    headlines.append(headline)


print(headlines)

hl=open("headlines.txt","a")

for headline in headlines:
    hl.write(headline+"\n")



