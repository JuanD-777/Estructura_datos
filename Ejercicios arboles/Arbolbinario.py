class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda= izquierda
        self.derecha= derecha

class Arbol_binario:
    def __init__(self):
        self.raiz =None

    def insertar(self,valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_con_recurcion(self.raiz,valor)


    def _insertar_con_recurcion(self, nodo_sumama, valor):

        if valor < nodo_sumama.valor:
            if nodo_sumama.izquierda is None:
                nodo_sumama.izquierda = Nodo(valor)

            else:
                self._insertar_con_recurcion(nodo_sumama.izquierda, valor)
        else:
            if nodo_sumama.derecha is None:
                nodo_sumama.derecha = Nodo(valor)
            else:
                self._insertar_con_recurcion(nodo_sumama.derecha,valor)

    def inorden(self):
        self._inorden_R(self.raiz)

    def _inorden_R(self, nodo):
        if nodo:
            self._inorden_R(nodo.izquierda)
            print(nodo.valor, end=' ')

            self._inorden_R(nodo.derecha)


    def imprimir_arbol(self, nodo=None, prefijo="", es_izquierdo=True):
        if nodo is None:
            nodo = self.raiz

        if nodo.derecha:
            self.imprimir_arbol(nodo.derecha, prefijo + ("│   " if es_izquierdo else "    "), False)

        print(prefijo + ("└── " if es_izquierdo else "┌── ") + str(nodo.valor))

        if nodo.izquierda:
            self.imprimir_arbol(nodo.izquierda, prefijo + ("    " if es_izquierdo else "│   "), True)



#apliacada la funcion buscar del punto 2

def buscar(nodo, valor):
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    elif valor<nodo.valor:
        return buscar(nodo.izquierda,valor)
    else:
        return buscar(nodo.derecha, valor)


Arbol = Arbol_binario()
valores =[ 20 , 10, 30, 5, 15, 25, 35]

for valor in valores:
    Arbol.insertar(valor)

print("Valores en orden:")
Arbol.inorden()

print("Árbol estructurado:")
Arbol.imprimir_arbol()

valor_buscado = 9
if buscar(Arbol.raiz, valor_buscado):
    print(f"El valor {valor_buscado} sí está en el árbol.")
else:
    print(f"El valor {valor_buscado} no está en el árbol.")



