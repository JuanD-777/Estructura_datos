from typing import Optional

class tarea: 
    def __init__(self,descripcion:str,prioridad:int,Fechavencimiento:int):
        self.descripcion=descripcion
        self.prioridad=prioridad
        self.Fechavencimiento=Fechavencimiento
        self.siguiente=None # apuntador al siguiente nodo

class Lista_tareas: 
    def __init__(self):
        self.cabeza= None #aqui inicia la lista


    def agregar(self, descripcion, prioridad, Fechavencimiento):
        nueva_tarea=tarea(descripcion,prioridad,Fechavencimiento)
        if not self.cabeza or prioridad < self.cabeza.prioridad:
            nueva_tarea.siguiente = self.cabeza
            self.cabeza = nueva_tarea
        else:
            nodo_actual=self.cabeza
            while nodo_actual.siguiente and nodo_actual.siguiente.prioridad <= prioridad:
                nodo_actual = nodo_actual.siguiente
            nueva_tarea.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nueva_tarea
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
                print(f"Tarea '{descripcion}' eliminada con exito")
                return
            anterior=actual
            actual=actual.siguiente
        return f"Tarea '{descripcion}' no encontrada"
    
    def mostrar(self):
        actual = self.cabeza
        if not actual:
            print("No hay tareas en la lista")
            return
        while actual:
            print(f"Descripción: {actual.descripcion}, prioridad: {actual.prioridad}, Fecha de vencimiento: {actual.Fechavencimiento}")
            actual = actual.siguiente  # con esto podemos Avanzar en la lista


    def buscar(self,descripcion):
        actual=self.cabeza
        while actual: 
            if actual.descripcion == descripcion:
                print(f"Tarea encontrada: {actual.descripcion}, prioridad: {actual.prioridad}, Fecha de vencimiento: {actual.Fechavencimiento}")
                return
            actual=actual.siguiente
        print(f"Tarea '{descripcion}' no encontrada")


    def completar(self,descripcion):
        return self.eliminar(descripcion) # "eliminar" equivale a completar la lista
    
    #ejemplos de uso
lista =Lista_tareas()
lista.agregar("Estudiar", 1, "2024-03-15")
lista.agregar("Comprar comida", 2, "2024-03-10")
lista.agregar("Hacer ejercicio", 3, "2024-03-20")

lista.mostrar()
lista.eliminar("Comprar comida")
lista.mostrar()
lista.buscar("Estudiar")
lista.completar("Hacer ejercicio")
lista.mostrar()