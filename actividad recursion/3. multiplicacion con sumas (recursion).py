def multiplicar (a,b):
    if b==0:
      return 0
    if b<0 :
      return -multiplicar(a,-b)
    return a + multiplicar (a,b-1)

a=int(input("ingrese el primer numero: " ))
b=int(input("ingrese el segundo numero: " ))
resultado = multiplicar(a,b)
print(f"la multiplicacion de a x b es: {resultado}")