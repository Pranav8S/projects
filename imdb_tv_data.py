import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np

url="https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

response=requests.get(url)

print(response)

tv = open("Top_250_TV_Shows.html","r+",encoding="utf8")

print(tv)
    
soup=BeautifulSoup(tv.read(),"html.parser")
print(soup)

with open ("Top_250_TV_Shows.html","r+",encoding="utf8") as file: 
    file.write(soup.prettify())



#names
tv_names=[]
for element in soup.find_all("h3"):
    if re.search("^[0-9]",element.text.strip()):
        tv_names.append(element.text.strip())

print(tv_names)



#ratings
tv_ratings=[]

for element in soup.find_all(class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"):
    tv_ratings.append(element.get_text(strip="True"))

print(tv_ratings)



#release_info
tv_releases=[]

elements=soup.find_all("div",{"class":"sc-b51a3d33-5 ibuRZu cli-title-metadata"})
print(elements)

for element in elements:
    tv_releases.append(element.get_text(strip="True"))

print(tv_releases)


#check count
print(len(tv_names))
print(len(tv_ratings))
print(len(tv_releases))



data_=[]
data_.append(tv_names)
data_.append(tv_ratings)
data_.append(tv_releases)

print(data_)

data=np.array(data_)

print(data)

dataT=np.transpose(data)
print(dataT)

df=pd.DataFrame(dataT)

print(df)

headers=["tv_names","tv_ratings","tv_releases"]
df.columns=headers

print(df.columns)

print(df.info)

print(df.describe(include="all"))

df[["tv_ratings","no_of_votes"]]=df["tv_ratings"].str.split("(",expand=True)

df=df[['tv_names', 'tv_ratings', 'no_of_votes', 'tv_releases']]

df["no_of_votes"]=df["no_of_votes"].str.replace(")","")

print(df["tv_releases"])


# below result would give the first row insted of first part of the split
#print(df["tv_releases"].str.split("eps")[0])

print(df["tv_releases"].str.split("eps").str[0])


df["tv_releases"]=df["tv_releases"].str.split("eps").str[0]

print(df)
print(df.columns)

#df.drop(labels="no_of_episodes",axis=1,inplace=True)


list=[]
list=df["tv_releases"].str.split("–").str[1]

list=list.str.strip()
list.replace(np.NaN,0,inplace=True)

print(list)

print(list[246])
print(len(str(list[246])))

condition=[item for item in list if (len(str(item))>7)]
print(condition)

condition=[item for item in list if (len(str(item))==4)]
print(condition)



list_eps=[]
for item in list:
    if len(str(item))>4:
        list_eps.append(item[4:])
    else :
        list_eps.append(item)
print(list_eps)

df["no_of_episodes"]=list_eps

print(df)    

df["tv_releases"]=df["tv_releases"].str.split("–").str[0]

print(df)   

list_=[]
list_=df["tv_releases"].tolist()

print(list_)

## getting release year for all the tv shows
list_release=[]
for item in list_:
    list_release.append(item[:4])

print(list_release)

df["tv_releases"]=list_release

print(df)


## getting the remianing episodes which were merged with year

list_eps=[]
for item in list_:
    if len(str(item))>4:
        list_eps.append(item[4:])
    else:
        list_eps.append(0)

print(list_eps)

list_present=[]
list_present=df["no_of_episodes"].tolist()
print(list_present)

type(list_present)

list_final=[]

for i,item in enumerate(list_present):
    if item==0:
        list_final.append(list_eps[i])
    else:
        list_final.append(list_present[i])

print(list_final)
len(list_final)

df["no_of_episodes"]=list_final

df.rename(columns={"tv_releases":"release_year"},inplace=True)

df["no_of_episodes"]=df["no_of_episodes"].str.strip()

## splitting name into ranking and name

df["ranking"]=df["tv_names"].str.split(".",expand=True)[0]

df["tv_names"]=df["tv_names"].str.split(".",expand=True)[1]

list__=df["tv_names"].tolist()

list___=[]
for item in list__:
    list___.append(item[1:])
print(list___)

df["tv_names"]=list___

df=df[['ranking','tv_names', 'tv_ratings', 'no_of_votes', 'release_year','no_of_episodes']]


#replace M and K with 0s in no_of_votes

df["no_of_votes"]=df["no_of_votes"].str.replace("M", "000000")
df["no_of_votes"]=df["no_of_votes"].str.replace("K", "000")
df["no_of_votes"]=df["no_of_votes"].str.replace(".", "")

# modifying df for items that had no of votes as decimal like 2.2M
df[df["no_of_votes"].apply(lambda x:len(x)>7)]

df["no_of_votes"][12]=2200000
df["no_of_votes"][101]=1300000

print(df)

print(df.dtypes)

df[["ranking","no_of_votes","no_of_episodes","release_year"]]=df[["ranking","no_of_votes","no_of_episodes","release_year"]].astype("int")
df["tv_ratings"]=df["tv_ratings"].astype("float")

df.to_csv("Top_250_TV_Shows.csv",index=False)

df.columns


### operations

for row in df.itertuples(index=True):
    #print(len(row[2].split()))
    if len(row[2].split())==1:
        print(f'{row[2]}')


df_custom_filter=df[(df["ranking"]>8.5) & (df["no_of_votes"]>250000) & (df["release_year"]>2000)]

(df_custom_filter.sort_values(["no_of_votes","tv_ratings"],ascending=False)[["tv_names","no_of_votes","tv_ratings","no_of_episodes"]])

(df_custom_filter.sort_values(["tv_ratings","ranking"],ascending=[False,True])[["tv_names","tv_ratings","ranking"]])

df_temp=df[(df["no_of_votes"]<100000)&(df["tv_ratings"]>9)]

print(df_temp[["tv_names","ranking"]])


dftemp=df[df["tv_names"].apply(lambda x:"the" in x.lower().split())]

print(dftemp["tv_names"])


df_temporary=df.loc[df["tv_names"].str.contains("^The", regex=True)]

print(df_temporary["tv_names"])


condition=df["tv_names"].str.contains("^The", regex=True)
df_temporary=df
#df.loc[row,column]
df_temporary.loc[condition,"tv_names"]="test"

print(df_temporary)

#above code is similar to below boolean masked code

print("############################################")

df_temporary.loc[df["tv_names"].str.contains("^The", regex=True),"tv_names"]="test"

print(df_temporary)


## group by
df.groupby("release_year").mean(numeric_only=True).sort_values("tv_ratings",ascending=False)

df["count"]=1
df.groupby(["release_year","tv_ratings"]).count()["count"].sort_values(ascending=False)
