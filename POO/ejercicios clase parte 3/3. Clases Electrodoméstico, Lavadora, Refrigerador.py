class Electrodomestico:
    marca: str
    modelo: str
    consumoEnergético: str
    
    def __init__(self, marca: str, modelo: str, consumoEnergético: str):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergético = consumoEnergético
    
    def encender(self) -> str:
        return "El electrodoméstico está encendido."

class Lavadora(Electrodomestico):
    capacidad: int
    
    def __init__(self, marca: str, modelo: str, consumoEnergético: str, capacidad: int):
        super().__init__(marca, modelo, consumoEnergético)
        self.capacidad = capacidad
    
    def encender(self) -> str:
        return f"La lavadora {self.marca} {self.modelo} ha iniciado el ciclo de lavado."

class Refrigerador(Electrodomestico):
    tieneCongelador: bool
    
    def __init__(self, marca: str, modelo: str, consumoEnergético: str, tieneCongelador: bool):
        super().__init__(marca, modelo, consumoEnergético)
        self.tieneCongelador = tieneCongelador
    
    def encender(self) -> str:
        return f"El refrigerador  {self.marca} {self.modelo} está regulando la temperatura."


lavadora1 = Lavadora("LG", "X100", "Bajo", 10)
refrigerador1 = Refrigerador("Samsung", "Frost200", "Medio", True)
print(lavadora1.encender())
print(refrigerador1.encender())