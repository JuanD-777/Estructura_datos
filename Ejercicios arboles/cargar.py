import pandas as pd

class Hospital:
    def __init__(self, nombre:str, nit: int, sede: str, municipio: str):
        self.nombre = nombre
        self.nit = nit
        self.sede = sede
        self.municipio = municipio

    def __str__(self):
       return f"nombre: {self.nombre}, nit: {self.nit}, sede: {self.sede}, municipio: {self.municipio}"

class Nodo:
    def __init__(self, hospital):
        self.hospital = hospital
        self.izquierda = None
        self.derecha = None  



class Arbolhospital:
    def __init__(self):
      self.raiz=None

    def insertar(self, hospital):
        if self.raiz is None:
            self.raiz = Nodo (hospital)
        else:
            self._insertar_recursion(self.raiz, hospital)

    def _insertar_recursion(self, nodo, hospital):
        if hospital.nit < nodo.hospital.nit:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(hospital)
            else:
               self._insertar_recursion(nodo.izquierda, hospital)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(hospital)
            else:
                self._insertar_recursion(nodo.derecha, hospital)


    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.hospital)
            self.inorden(nodo.derecha)


def buscar_hospital(arbol, nit_buscado): 
    return _buscar_recursion(arbol.raiz, nit_buscado)

def _buscar_recursion(nodo,nit_buscado):
    if nodo is None:
        return None
    if nit_buscado == nodo.hospital.nit:
        return nodo.hospital
    elif nit_buscado < nodo.hospital.nit:
        return _buscar_recursion(nodo.izquierda, nit_buscado)
    else:
        return _buscar_recursion(nodo.derecha, nit_buscado)


hospitales = pd.read_csv('/workspaces/Estructura_datos/Ejercicios arboles/Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426.csv')
hospitales.rename(columns={
    'Razón Social Organización': 'nombre',
    'Número NIT': 'nit',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio'
}, inplace=True)
hospitales['nit'] = hospitales ['nit'].str.replace(',','')
hospitales['nit'] = hospitales ['nit'].astype(int)
print(hospitales.head())
print(hospitales.dtypes)
print(hospitales.columns)
print(hospitales['nit'])

arbol = Arbolhospital()

for index, row in hospitales.iterrows():
    hospital = Hospital(
        nombre=row['nombre'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    arbol.insertar(hospital)

print("Hospitales ordenados por NIT:")
arbol.inorden(arbol.raiz)


nit_a_buscar = int(input("Ingrese el NIT del hospital a buscar: "))
resultado = buscar_hospital(arbol, nit_a_buscar)

if resultado:
    print("🏥 Hospital encontrado:")
    print(f"Nombre de la organización: {resultado.nombre}")
    print(f"Nombre de la sede: {resultado.sede}")
    print(f"Municipio: {resultado.municipio}")
else:
    print("❌ Hospital no encontrado.")