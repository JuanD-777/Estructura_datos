class Libro:
    titulo: str
    autor: str
    genero: str
    añoDePublicacion: int

    def __init__(self, titulo: str, autor: str, genero: str, añoDePublicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.añoDePublicacion = añoDePublicacion

    def mostrar_detalles(self):
        print(f"el libro {self.titulo} por {self.autor}, Género: {self.genero}, Publicado en {self.añoDePublicacion}")

libro1 = Libro("1984", "George Orwell", "Distopía", 1949)
libro1.mostrar_detalles()