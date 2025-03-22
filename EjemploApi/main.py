from typing import Union

from fastapi import FastAPI
from funciones import mostrartexto

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ejemplo")
def ejemplo_paquete():
    retorno=mostrartexto()
    return {"mensaje": retorno}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}