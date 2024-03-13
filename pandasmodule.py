import pandas as pd
import re

# read csv data into a dataframe
df=pd.read_csv("pokemon_data.csv")

# for files with large amounts of data loading entire data would hog up memory and cause performance issues
# so we can specify how many rows we want to load to overcome this issue
# df=pd.read_csv("pokemon_data.csv",nrows=100) #nrows or chunksize


i=0
for df in pd.read_csv("pokemon_data.csv",chunksize=100):
    i=i+1
    print(f"CHUNK NO - {i}")
    print(df)  



# different ways to print data 
print(df)
print("############################################")
print(df.head(10))
print("############################################")
print(df.tail(10))
print("############################################")

# different ways to get more information/details about the data
print(df.describe(include="all"))
print("############################################")
print(df.info())
print("############################################")
print(df.count())
print("############################################")

#drop column "#"
df.drop("#",axis=1,inplace=True)
print(df)

# print(df.index)



"""


.-----------> columns axis 1
|
|
|
|
v
rows
axis 0


"""
pattern='[\w\.-]+'

list=[]


### boolean masking


df_HP = df["HP"]
print(df_HP)

condition = df["HP"] > 50

print(df[condition])

#or

print(df[df["HP"] > 50])




# to print columns
print(df.columns) ### headers
print("############################################")
print(df["Name"])
print(df["Name"][8])
print("############################################")
print(df[["Name","HP","Speed"]])
print("#######################******#####################")

# to print a row/data we use iloc (index-locator) and loc(label based locator)

print(df.iloc[2])
print("############################################")
# df.iloc[rows,columns]
print(df.iloc[[502],[2]])
print("############################################")
print(df.iloc[[1,798],[0,9]])
print("############################################")
print(df.iloc[3:500:111])
print("############################################")
print(df.iloc[[4],[1]])
print(df.iloc[4,1])
print("############################################")



# df.loc[rows,columns]
print(df.loc[df["Generation"]==4])
print("############################################")
print(df.loc[[1,799],["Name","Legendary"]])
print("############################################")
print(df.loc[df["Type 1"]=="Grass"])
print("############################################")
print(df.loc[(df["Type 1"]=="Fire") & (df["HP"]>50)])
print("############################################")

#iterate through rows and print index/data[row]
for index,row in df.iterrows():
    print(index, row)
print("############################################")

for index,row in df.iterrows():
    print(index, row["Name"])
print("############################################")

for index,row in df.iterrows():
    print(index, row["Name"],row["HP"])
print("############################################")

#iterate through rows and print row number 
## iterating over dataframe is NOT recommended and generally not needed
## use apply() or vectorization (list comprehention, boolean masking, built-in numpy functions) insted
## itertuples() is faster and preserves dtypes

for row in df.itertuples(index=True):
    print(row)

for index,row in df.iterrows():
    print("index= ",index,end="\n")
    print(row)
    print("")
    
for i,row in enumerate(df.iterrows()):
    print(i+1, row)
print("############################################")




# sorting
print(df.sort_values("Name", ascending=False))
print("############################################")
print(df.sort_values(["Type 1","Name"], ascending=[True,False]))
print("############################################")

#making changes to the data
df["Total"]=df["HP"]+df["Attack"]+df["Defense"]+df["Speed"]

print(df)

df.drop(columns=["Total"],inplace=True)

print(df)

df["Total"]=df.iloc[:,[3,4,5,8]].sum(axis=1)

print(df)

print("############################################")


# rearrange columns

columns=list(df.columns)

cols=df.columns.values

print(columns,cols)

new_order=['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Speed', 'Total', 'Sp. Atk', 'Sp. Def', 'Generation', 'Legendary']

df=df[new_order]

# or

df=df[columns[0:6]+[columns[-4]]+[columns[-1]]+columns[6:8]+columns[9:11]]

print(df)


#saving file to csv
df.to_csv("modified_pokemon_data.csv",index=False,sep=",")

print("############################################")


### filtering

df1=df.loc[(df["Type 1"]=="Fire")|(df["Type 2"]=="Grass") & (df["HP"]>50)]

print(df1[["Name","Type 1","Type 2","HP"]])

df1.reset_index(drop=True,inplace=True)

print(df1[["Name","Type 1","Type 2","HP"]])


print("############################################")


df2=df.loc[(df["Type 1"]=="Fire")|(df["Type 1"]=="Grass") & (df["HP"]>50)]

print(df2[["Name","Type 1","HP"]])

df2.reset_index(drop=True,inplace=True)

print(df2[["Name","Type 1","HP"]])

print("############################################")

### any results than contain "Mega" like "Mega Charizard"
print(df[df['Name'].str.contains('Mega')])
### results that contains only "Mega" and not Mega Charizard"
print(df[df["Name"].isin(["Mega"])])
### inverse of above result
print(df[~df["Name"].isin(["Mega"])])

print("############################################")

print(df[df["Name"].isin(["Meganium"])])

dfHP_=df[(df["HP"]>50) & (df["HP"]<100)]

print(dfHP_["HP"])

print("############################################")


### regex based filtering

print(df[df['Name'].str.contains('saur|der',regex=True)])

print(df[df['Name'].str.contains('s$',regex=True)])

print(df[df['Name'].str.contains('^C',flags=re.I,regex=True)])

print(df[df['Name'].str.contains("^pi[a-z]*",flags=re.I,regex=True)])

print("############################################")



### conditional changes

condition=df["Type 1"]=="Fire"
#df.loc[row,column]
df.loc[condition,"Type 1"]="Flamer"

print(df)

#above code is similar to below boolean masked code

print("############################################")

df.loc[df["Type 1"]=="Fire","Type 1"]="Flamer"


condition_new=df["Type 1"]=="Flamer"

df.loc[condition,"Legendary"]="True"
 
print(df)

print("############################################")

condition=(df["Total"] > 60) & (df["Legendary"] == "True")

df.loc[condition,["Generation","Type 2"]] = ["Test 1","Test 2"]

print(df[["Type 2","Generation"]])


### aggregate statistics (group_by)

df.groupby(["Type 1"]).mean(numeric_only=True).sort_values("HP",ascending=False)

## in the below code we create a column called count and assign it the value 1 for all rows.
## this acts as a weight for each row
## so when this is used with groupby the similar attributes are clubbed together
## which results in summation of counts


df["count"]=1
df.groupby(["Type 1","Type 2"]).count()["count"]

df.drop("count",axis=1,inplace=True)



## loading and performing operations on chunks of the data
new_df=pd.DataFrame(columns=df.columns)

i=0
for df in pd.read_csv("pokemon_data.csv",chunksize=100):
    i=i+1
    print(f"CHUNK NO - {i} loaded")
    result=df.groupby(["Type 1","Type 2"]).count()
    
    new_df=pd.concat([new_df,result])

print(new_df)

new_df.columns

list_of_grouped_items=new_df.T.iloc[0].tolist()    

print(list_of_grouped_items)