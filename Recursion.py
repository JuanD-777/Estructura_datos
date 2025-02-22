numero = 5
resultado:int
def factorial (n:int)->int:
    for i in range (1,n):
        resultado= resultado*i
    return resultado
print(factorial(numero))