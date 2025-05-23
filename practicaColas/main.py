from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "questions": TicketController(),
    "advisor": TicketController(),
    "cashier": TicketController(),
    "others": TicketController()
}

# Endpoint to create a turn
@app.post("/ticketCreate")
def create_turn(turn: Ticket):
    add_queue(turn, ticketTypes)
    return {"message": "Turn created successfully", "turn_data": turn}

# Endpoint to check the next turn without removing it
@app.get("/ticketPeek")
def peek_next_turn(type: str):
    if type in ticketTypes:
        next_turn = ticketTypes[type].peek()
        if next_turn:
            return {"message": "The next turn is", "turn_data": next_turn}
        else:
            return {"message": "No turns in queue"}
    return {"message": "Invalid turn type"}

# Endpoint to get the next turn
@app.get("/ticketNext")
def get_next_turn(type: str):
    if type in ticketTypes:
        next_turn = ticketTypes[type].dequeue()
        if next_turn:
            return {"message": "The next turn is", "turn_data": next_turn}
        else:
            return {"message": "No turns in queue"}
    return {"message": "Invalid turn type"}

# Endpoint to list turns in queue by turn type
@app.get("/ticketList")
def list_queue_turns(type: str):
    if type in ticketTypes:
        turns = []
        current = ticketTypes[type].head
        while current:
            turns.append(current.data)
            current = current.next

        if turns:
            return {"message": "List of pending turns", "turn_data": turns}
        else:
            return {"message": "No pending turns"}
    
    return {"message": "Invalid turn type"}

# Other existing endpoints
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
