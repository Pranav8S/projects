from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    description: str|None=None
    price: int
    tax: float|None=None
    flg: bool

@app.get('/item/{id}/')
def create_item(id,item): #,item:Item
    # this function will perform some operation/processing on the data that it will receive
    item_dict=dict(item)
    return f'data for {id} is 0'

@app.post('/item/{id}')
def send_item(id):
    pass

