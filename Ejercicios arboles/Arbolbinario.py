class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda= izquierda
        self.derecha= derecha

class Arbol_binario:
    def __init__(self, raiz):
        self.raiz =raiz

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
        self._inorden_recursivo(self.raiz)
