class Producto:
    nombre: str
    precio: int
    cantidadDisponible: int

    def __init__(self, nombre: str, precio: float, cantidadDisponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible

    def calculo_total(self, cantidad: int):
        return self.precio * cantidad

producto1 = Producto("Laptop", 800, 10)
print(producto1.calculo_total(2))