# 0 = libre
# 1 = muro
# 3 = ruta
# 4 = Camino sin salida
# 2 = salida

tablero = [
    [1, 0, 1, 1, 2],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def mostrar(tablero):
    simbolos = {0: "0", 1: "#", 2: "E", 3: "X", 4: "."}
    for fila in tablero:
        print(" ".join(simbolos[celda] for celda in fila))
    print()

def valido(i, j):
    return 0 <= i < len(tablero) and 0 <= j < len(tablero[0])  # Verifica límites

def buscar_con_pila(tablero, start_i, start_j):
    stack = [(start_i, start_j)]  # Pila con la posición inicial
    movimientos = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Arriba, Izquierda, Abajo, Derecha
    
    while stack:
        i, j = stack.pop()  # se saca la última posición añadida a la pila

        if not valido(i, j) or tablero[i][j] in (1, 3, 4):  
            continue  # Si es un muro o ya fue visitado, saltamos

        if tablero[i][j] == 2:  # Si encontramos la salida
            print("¡Encontró la salida!")
            mostrar(tablero)
            return True

        tablero[i][j] = 3  # Marcar como parte de la ruta

        # Agregar las posibles direcciones a la pila
        for di, dj in movimientos:
            ni, nj = i + di, j + dj
            if valido(ni, nj) and tablero[ni][nj] not in (1, 3, 4):
                stack.append((ni, nj))
    
    # Marcar rutas sin salida
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 3:
                tablero[i][j] = 4  # Marcar caminos sin salida
    
    print("No se encontró la salida.")
    mostrar(tablero)
    return False

# Ejecutamos la búsqueda con pila desde la posición inicial (4,0)
buscar_con_pila(tablero, 4, 0)
