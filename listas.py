numeros=list()
Continuar: bool = True

def agregar (numero:int) -> None:
  numeros.append(numero)

def eliminar() -> None:
  numeros.pop()

while Continuar:
  print ("seleccione una opcion")
  print  ("1. agregar un numero")
  print  ("2. eliminar un numero")
  print  ("3. salir")
  
  opcion = int(input())

  if opcion == 3:
    Continuar = False
  if opcion == 1: 
   print ("ta bien")