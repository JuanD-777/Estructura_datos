from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

# Endpoint para crear un turno
@app.post("/ticketCreate")
def crear_turno(turno: Ticket):
    add_queue(turno, ticketTypes)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

# un Endpoint nuevo para consultar el siguiente turno sin eliminarlo
@app.get("/ticketPeek")
def consultar_siguiente_turno(tipo: str):
    if tipo in ticketTypes:
        siguiente_turno = ticketTypes[tipo].peek()
        if siguiente_turno:
            return {"mensaje": "El siguiente turno es", "datos_turno":siguiente_turno}
        else:
            return {"mensaje": "No hay turnos en la cola"}
        
    return {"mensaje": "Tipo de turno no valido"}



# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    if tipo in ticketTypes:
        siguiente_turno = ticketTypes[tipo].dequeue()
        if siguiente_turno:
            return {"mensaje": "El siguiente turno es", "datos_turno": siguiente_turno}
        else:
            return {"mensaje": "No hay turnos en la cola"}
    return {"mensaje": "Tipo de turno no válido"}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    if tipo in ticketTypes:
        turnos = []
        current = ticketTypes[tipo].head
        while current:
            turnos.append(current.data)
            current = current.next

        if turnos:
            return {"mensaje": "Lista de turnos pendientes", "datos_turnos": turnos}
        else:
            return {"mensaje": "No hay turnos pendientes"}
    
    return {"mensaje": "Tipo de turno no válido"}

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

