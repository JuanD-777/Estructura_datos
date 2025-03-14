from typing import Optional



class Animal:
   def __init__(self,nombre:str,tipo:str,edad:int)->None:
        self.nombre=nombre
        self.tipo=tipo
        self.edad=edad
        
def set_nombre(self,nombre:str)->None:
        self.nombre=nombre
       
       
def get_nombre(self)->str:
        return self.nombre 
        
class Node:
    def __init__(self,animal:Animal)->None:
        self.animal=animal
        self.next:Optional["Node"]=None
        
class listaenlazada:
    def __init__(self)->None:
        self.cabeza:Optional["Node"]=None
        
    def agregar(self,animal:Animal)->None:
         nodo:Node=Node(animal)
         if self.cabeza is None:
            self.cabeza=nodo
         else:
            nodo_actual=self.cabeza
            while nodo_actual.next is not None:
               nodo_actual=nodo_actual.next
            nodo_actual.next=nodo
            
    def imprimir(self)->None:
        nodo_actual=self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.animal.nombre)
            nodo_actual=nodo_actual.next 
            
animal1=Animal('firulais','perro',5)
animal2=Animal('michi','gato',3)
animal3=Animal('pepe','perico',1)
animal4=Animal('beto','pez',1)
lista=listaenlazada()
lista.agregar(animal1)
lista.agregar(animal2)
lista.agregar(animal3)
lista.agregar(animal4)
lista.imprimir()
    
    
        
    