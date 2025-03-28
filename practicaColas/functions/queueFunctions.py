from model.ticket import Ticket
from controller.ticketController import TicketController


def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    opciones = {
        "dudas", 
        "asesor",
        "caja",
        "otros"
     }
    
    if ticket.type not in opciones:
        print("el Tipo de ticket no válido")
        return 
    if ticket.type not in ticketTypes:
        ticketTypes[ticket.type] = TicketController.enqueue()    

    ticketTypes[ticket.type].enqueue(ticket)
    print(f"ticket de tipo '{ticket.type}")

print("añadir a la cola") 
print("ticket añadido a la cola")