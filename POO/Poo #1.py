class vehiculo:
    color: str 
    modelo:int
    cilindraje:int
    numero_ruedas: int
    combustible: int
    
    def __init__(self,marca:str,combustible:int)->None:
        self.marca=marca
        self.combustible=combustible
    
    def __str__(self):
        return f"lamarca del vehiculo es: {self.marca} y el nivel de combustible es: {self.combustible}"
    
    def encender (self):
     pass

    def acelerar(self):
       pass

    def frenar(self):
       pass

    def apagar(self):
       pass

vehiculo1=vehiculo('mazda',80)
print(vehiculo1)