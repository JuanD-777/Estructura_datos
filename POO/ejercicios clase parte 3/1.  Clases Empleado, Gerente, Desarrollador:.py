class Empleado:
    nombre: str
    salario: int
    departamento: str
    
    def __init__(self, nombre: str, salario: int, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self) -> str:
        return f"{self.nombre} está trabajando."

class Gerente(Empleado):
    equipo: list
    
    def __init__(self, nombre: str, salario: int, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo
    
    def trabajar(self) -> str:
        return f"{self.nombre} está supervisando al equipo."

class Desarrollador(Empleado):
    lenguajeDeProgramacion: str
    
    def __init__(self, nombre: str, salario: int, departamento: str, lenguajeDeProgramacion: str):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion
    
    def trabajar(self) -> str:
        return f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}."


emp = Empleado("Juan", 3000, "General")
ger = Gerente("Ana", 5000, "TI", ["Juan", "Pedro"])
des = Desarrollador("Pedro", 4000, "TI", "c++")
print(emp.trabajar())
print(ger.trabajar())
print(des.trabajar())