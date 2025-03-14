from typing import Optional

class tarea: 
    def __init__(self,descripcion:str,Prioridad:int,FechaVencimiento:int)
        self.descripcion=descripcion
        self.Prioridad=Prioridad
        self.FechaVencimiento=FechaVencimiento
        self.siguiente=None # apuntador al siguiente nodo

class ListaTeras: 
    def __init__(self):
        self.cabeza= None #aqui inicia la lista


    def agregar(self, descripcion, prioridad, Fechavencimiento):
        nueva_tarea=tarea(descripcion,prioridad,Fechavencimiento)
        if not self.cabeza or prioridad < self.cabeza.prioridad:
            nueva_tarea.siguiente=self.cabeza
            self.cabeza=nueva_tarea
        else:
            nodo_actual=self.cabeza
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual=actual.siguiente
            nueva_tarea.siguiente=actual.siguiente
            actual.siguiente=nueva_tarea
            print("Tarea agregada con exito")

    def eliminar(self,descripcion):
        actual=self.cabeza
        anterior=None
        while actual:
            if actual.descripcion == descripcion:
                if anterior:
                    anterior.siguiente=actual.siguiente
                else:
                    self.cabeza=actual.siguiente
                return f"Tarea '{descripcion}' eliminada con exito"
            anterior=actual
            actual=actual.siguiente
        return f"Tarea '{descripcion}' no encontrada"
            
    def