class vehiculo:
    marca:str
    color: str 
    modelo:int
    cilindraje:int
    numero_ruedas: int
    combustible: int
    tipo: str
    
    
    def __init__(self,marca:str,combustible:int,tipo:str)->None:
        self.marca=marca
        self.combustible=combustible
        self.tipo=tipo
        
    
    def __str__(self):
        return f"el vehiculo es un/una:{self.tipo} lamarca del vehiculo es: {self.marca} y el nivel de combustible es: {self.combustible}"
    
    def encender (self):
       if self.combustible<=10:
          return("el vehiculo tiene poco combustible, por favor llenalo")
       else: 
         return("el vehiculo este listo para conducirse")
        
         
    def acelerar(self):
       if self.combustible <= 0:
          return "el vehiculo no puede moverse, no tiene combustible"
       print ("el vehiculo ha comenzado a moverse.")
       while self.combustible >0:
          self.combustible -=5
          print(f"Nivel de combustible: {self.combustible}")
       if self.combustible <=10:
          print("advertencia: nivel de combuustible bajo")
       if self.combustible ==0:
          print("el vehiculo se ha detenido por falta de combustible")
    def frenar(self):
       pass

    def apagar(self):
       pass

class moto(vehiculo):
    pass

class carro(vehiculo):
   pass

vehiculo1=vehiculo('mazda', 80 , 'generico')
print(vehiculo1)
print(vehiculo1.encender())
vehiculo1.acelerar()

moto1 = moto('ducati', 1 , 'moto')
print(moto1)
print(moto1.encender())
moto1.acelerar()

carro1= carro('bmw', 20 , 'carro')
print(carro1)
print(carro1.encender())
carro1.acelerar()
