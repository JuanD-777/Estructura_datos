from model.ticket import Ticket
from controller.ticketController import TicketController


def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    opciones = {
       "questions", 
        "advisor",
        "cashier",
        "others"

     }
    
    if ticket.type not in opciones:
        print("Invalid ticket type")
        return 
    if ticket.type not in ticketTypes:
        ticketTypes[ticket.type] = TicketController()   

    ticketTypes[ticket.type].enqueue(ticket)
    print(f"Ticket of type '{ticket.type}' added to queue")

