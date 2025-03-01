persona=dict()
continuar: bool=True
 

def agregar_valor (clave:str,valor:str): 
    persona.update({clave:valor})

def eliminar() :
    persona.popitem()

while continuar: 
 print("escoge un opcion")
 print  ("1. agregar un valor")
 print  ("2. eliminar un valor")
 print  ("3. salir")

 opcion = int(input())

 if opcion == 3:
     continuar=False
 elif opcion == 1:
        clave = input("Ingresa la clave: ")
        valor = input("Ingresa el valor: ")
        agregar_valor(clave, valor)
        print(f"Diccionario actualizado: {persona}")
 elif opcion == 2:
     eliminar(clave,valor)
