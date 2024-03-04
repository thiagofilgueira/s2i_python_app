from typing import Union

import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/show")
def get_connectors(url: Union[str, None] = None):
    data = {}
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Erro na chamada API. Código de status: {response.status_code}")
        print(response.text)
    return data
