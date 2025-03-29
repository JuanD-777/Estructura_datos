from model.ticket import Ticket
from model.node import Node

class TicketController:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self) -> bool:
        return self.head == None 
    
    def enqueue(self, ticket: Ticket) -> None:
        if ticket.priority_attention is None or ticket.priority_attention is False:
            ticket.priority_attention = ticket.age >= 60

        node = Node(ticket, ticket.priority_attention)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            if current.priority < node.priority:
                node.next = current
                self.head = node
            else:
                while current.next is not None and current.next.priority >= node.priority:
                    current = current.next
                node.next = current.next
                current.next = node     

    def dequeue(self) -> Ticket:
        if self.is_empty():
            return None
        else:
            ticket = self.head.data
            self.head = self.head.next
            return ticket
        
    def peek(self) -> Ticket:
        if self.is_empty():
            return None
        else:
            return self.head.data
    
    def print_queue(self) -> None:
        current = self.head
        while current is not None: # Ajustado para usar el "is not None"
            print(f"Turno: {current.data.turno}, Prioridad: {current.priority}")
            current = current.next
        print("Fin de la cola")