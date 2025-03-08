class FiguraGeometrica:
    def calcularArea(self) -> float:
        pass

class Triangulo(FiguraGeometrica):
    base: float
    altura: float
    
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def calcularArea(self) -> float:
        return f"El ara del triangulo es: {(self.base * self.altura) / 2}"

class Cuadrado(FiguraGeometrica):
    lado: float
    
    def __init__(self, lado: float):
        self.lado = lado
    
    def calcularArea(self) -> float:
        return f"El ara del triangulo es:{self.lado ** 2}"


triangulo1 = Triangulo(10, 5)
cuadrado1 = Cuadrado(4)
print(triangulo1.calcularArea())
print(cuadrado1.calcularArea())