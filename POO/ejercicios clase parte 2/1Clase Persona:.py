class Persona:
     nombre:str
     edad:int
     genero:str
   
     def __init__(self, nombre:str, edad:int, genero:str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
     def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.genero}.")


persona1=Persona('daniela','21','femenino')
print(persona1)
print(persona1.presentarse())