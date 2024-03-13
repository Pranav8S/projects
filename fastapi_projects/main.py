from fastapi import FastAPI

import time

from enum import Enum

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'hello world!',
            'status':'alive'}


list_=list(range(144,373,4))

@app.get('/testroute')
def testroute(item_id,m,n):
    if n!=None:
        return{
            f'msg for {item_id}':list_[m:n]
        }
    else: 
        return{
            f'msg for {item_id}':[list_[m:]]
        }
    return {time.time()}

@app.get('/homepage')
def homepage():
    return{
        'message':"you're home"
    }


dict1={
    'abc':'abc848',
    'xyz':'xyz5445',
    'file_':'C:\\Users\\Pranav\\OneDrive\\Documents\\.vscode\\python\\example.py'
}

@app.get('/files/{item_}')
def display_file(item_:str):
    if item_=='file_':
        with open(dict1['file_'],'r') as f:
            text = f.read()
            return{
                'msg':text
            }
    else:
        return{
            'msg':{dict1[item_]}
        }



@app.get('/items/101')
def items_101(): # type: ignore
    return{
        'msg':'this will be evaluated and displayed as special case'
    }




@app.get('/items/{item_id}')
def items(item_id:int, m:int=0, n:int|None=None):
    match item_id:
        case 1:
            return homepage()
        case _:
            return testroute(item_id,m,n)
             

@app.get('/items/111')
def items_101():
    return{
        'msg':'this wont be evaluated and wont be displayed as the above function will take precedence i.e ordering is imp'
    }

