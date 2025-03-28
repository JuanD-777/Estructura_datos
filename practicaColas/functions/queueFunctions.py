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
    
    if ticket.type not in opciones and ticket.type not in ticketTypes:
        print("el Tipo de ticket no válido")
        return  
    if ticket.type not in ticketTypes:
        ticketTypes[ticket.type] = TicketController.enqueue()    

    ticketTypes[ticket.type].enqueue(ticket)
    print(f"ticket de tipo '{ticket.type}")

    print("Añadir ticket a la cola")
    turno = input("Turno: ")
    prioridad = input("Prioridad: ")
    ticket = Ticket(turno, prioridad)
    TicketController.enqueue(ticket)  # Previously in this line the “t” in the TicketController was in lower case.
    print("Ticket añadido a la cola")