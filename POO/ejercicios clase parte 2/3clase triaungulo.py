class Rectangulo:
    base: int
    altura: int

    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return  f"el area es: {self.base * self.altura}"

    def calcular_perimetro(self):
        return f"el perimetro es: {2 * (self.base + self.altura)}"

rect1 = Rectangulo(10, 5)
print(rect1.calcular_area())
print(rect1.calcular_perimetro())
