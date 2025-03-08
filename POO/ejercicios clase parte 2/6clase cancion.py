class Cancion:
    titulo: str
    artista: str
    album: str
    duracion: float

    def __init__(self, titulo: str, artista: str, album: str, duracion: float):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def reproducir(self):
        print(f"Se esta reproduciendo '{self.titulo}' de {self.artista} duracion {self. duracion} minutos...")

cancion1 = Cancion("bones", "imagine dragons", "mercury", 2.46)
cancion1.reproducir()
