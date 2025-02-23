def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    
    signo = -1 if (a < 0) != (b < 0) else 1
    a, b = abs(a), abs(b)
    
    return signo * (1 + dividir(a - b, b)) if a >= b else 0

a = int(input("Ingrese el dividendo: "))
b = int(input("Ingrese el divisor: "))
print(f"El resultado de {a} / {b} es: {dividir(a, b)}")
