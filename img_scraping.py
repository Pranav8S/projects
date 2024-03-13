import os
import re
import requests
from bs4 import BeautifulSoup

sitemap="https://www.pngmart.com/sitemap.xml"

response = requests.get(sitemap)

xml=response.text

soup=BeautifulSoup(xml,"xml")

#print(soup.prettify())

site_maps=[]

for loc in soup.find_all("loc"):
    if "posts" in loc.text.strip():
        site_maps.append(loc.text.strip())

print(site_maps)

print("##########################################")

master_list=[]
#temp_list=[]

for url in site_maps:
    if "100" in url: 
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"xml")
        for loc in soup.find_all("loc"):
        #     temp_list.append(loc.text.strip())
            txt=loc.text.strip()

            if re.findall(".png$",txt):
                master_list.append(loc.text.strip()) 

print(len(master_list))

print("##########################################")

images={}
img=[]
i=0
for link in master_list:
    title=link.split("/")[-1]
    image=requests.get(link)

    path="./images"+"/"+title
    print(path)
    print(i)
    i=i+1

    with open(path,"wb") as file:
        file.write(image.content)

    # print(image.text)
    
    # print(image.content)





 