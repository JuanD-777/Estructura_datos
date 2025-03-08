class Circulo:
    import math
    radio: float

    def __init__(self, radio: float):
        self.radio = radio

    def AreaCirculo(self):
        return f"el area es: {self.math.pi * self.radio ** 2}"

    def circunferencia(self):
        return f"circunferencia: {2 * self.math.pi * self.radio}"

circulo1 = Circulo(7)
print(circulo1.AreaCirculo())
print(circulo1.circunferencia())