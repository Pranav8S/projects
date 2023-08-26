import requests
import sys
import json

#refer itunes api for url creation

url="https://itunes.apple.com/search?media=music&limit=10&term="

term=""

try:
    while True:
        term=sys.argv[1]
    
        if len(sys.argv)>2 :
            for arg in sys.argv[2:] :
                term=term+"+"+arg
        break

except IndexError:
        sys.exit("pass atlest 1 argument")
        
print(url+term)

print("")

response=requests.get(url + term)

data=response.json()

print(json.dumps(response.json(), indent=2))

print("")

#refer jsondictvalueiteration to know how the trackname value was iterated 
for each_key in data["results"]:
	print(each_key["trackName"])
        



