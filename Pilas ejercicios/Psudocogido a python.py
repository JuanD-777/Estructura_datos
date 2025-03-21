def apilar(pila, tope):
    if tope < 10:
        valor = int(input("Ingrese un valor: "))
        tope += 1
        pila[tope] = valor
        return tope
    else:
        print("Error: la pila está llena.")
        return tope

def desapilar(pila, tope):
    if tope > 0:
        print(f"Elemento eliminado: {pila[tope]}")
        tope -= 1
        return tope
    else:
        print("Error: la pila está vacía.")
        return tope

def mostrar_pila(pila, tope):
    if tope == 0:
        print("La pila está vacía.")
    else:
        print("Elementos en la pila:")
        for i in range(tope, 0, -1):
            print(pila[i])

# Main program
pila = [0] * 11  # Using index 1-10 to match the pseudocode
tope = 0

while True:
    print("1. Apilar")
    print("2. Desapilar")
    print("3. Mostrar pila")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))
    
    if opcion == 1:
        tope = apilar(pila, tope)
    elif opcion == 2:
        tope = desapilar(pila, tope)
    elif opcion == 3:
        mostrar_pila(pila, tope)
    elif opcion == 4:
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")