class Estudiante:
    nombre: str
    edad: int
    curso: str
    calificaciones: list

    def __init__(self, nombre: str, edad: int, curso: str):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion: float):
        if 0 <= calificacion <= 5:
            self.calificaciones.append(calificacion)
        else:
            print("Calificación fuera de rango. Debe estar entre  y 5.")

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0

    def aprobar(self):
        return "Aprobado" if self.calcular_promedio() > 2.9 else "Reprobado"

estudiante1=Estudiante("Ana", 20, "Matemáticas")
estudiante1.agregar_calificacion(3)
estudiante1.agregar_calificacion(5)
estudiante1.agregar_calificacion(2)
print(estudiante1.calcular_promedio())
print(estudiante1.aprobar())