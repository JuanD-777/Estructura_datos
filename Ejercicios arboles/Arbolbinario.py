#creacion del nodo, defidnicion del valor,direccion izquierda y la derecha 
class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda= izquierda #hijo izquierdo/menor
        self.derecha= derecha    #hijo derecho/mayor

#creacion de la clase que representa al arbol binario, empieza vacio
class Arbol_binario:
    def __init__(self):
        self.raiz =None  

    #metodo/funcion publico para ingresar un valor
    def insertar(self,valor):
        if self.raiz is None:  #si el arbol esta vacio
            self.raiz = Nodo(valor)   #el nuevo nodo sera su raiz
        else:
            self._insertar_con_recursion(self.raiz,valor) #si la raiz esta llena se insertara con recursion

   #metodo de recursion privado para insertar valores nuevos
    def _insertar_con_recursion(self, nodo_nuevo, valor): 

        if valor < nodo_nuevo.valor:   #si el nodo nuevo es menor, va a la izquierda
            if nodo_nuevo.izquierda is None:
                nodo_nuevo.izquierda = Nodo(valor) #si no existe izq. la crea

            else:
                self._insertar_con_recursion(nodo_nuevo.izquierda, valor) #si hay, sigue bajando
        else:
            if nodo_nuevo.derecha is None:   #si el nodo nuevo es mayor o igual se va la derecha
                nodo_nuevo.derecha = Nodo(valor) #si no hay nada en la der. se agrega
            else:
                self._insertar_con_recursion(nodo_nuevo.derecha,valor) #sigue bajando

 #metodo inorden
    def inorden(self):
        self._inorden_R(self.raiz)

#recorrido izquierda derecha
    def _inorden_R(self, nodo):
        if nodo:
            self._inorden_R(nodo.izquierda)
            print(nodo.valor, end=' ') # imprime el valor del nodo

            self._inorden_R(nodo.derecha)

 #metodo grafico  para imprimir el arbol
    def imprimir_arbol(self, nodo=None, prefijo="", es_izquierdo=True):
        if nodo is None:
            nodo = self.raiz  #si no se le da un nodo desde afuera, usara la raiz

        if nodo.derecha:
            #llama primero al hijo derecho (se imprime arriba)
            self.imprimir_arbol(nodo.derecha, prefijo + ("│   " if es_izquierdo else "    "), False)
             #imprime el nodo actual con algunos simbolos visuales
        print(prefijo + ("└── " if es_izquierdo else "┌── ") + str(nodo.valor))

        if nodo.izquierda:
         # Llama al hijo izquierdo (para imprimir abajo)
            self.imprimir_arbol(nodo.izquierda, prefijo + ("    " if es_izquierdo else "│   "), True)



#apliacada la funcion buscar del punto 2

def buscar(nodo, valor):
    if nodo is None:
        return False
    if nodo.valor == valor:    # Si el valor actual coincide, lo encontró
        return True
    elif valor<nodo.valor:    # Si es menor, busca a la izquierda
        return buscar(nodo.izquierda,valor)
    else:              # Si es mayor, busca a la derecha
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



