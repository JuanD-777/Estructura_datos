def multiplicar_con_sumas(a, b):
    resultado = 0
    for _ in range(abs(b)):  # Repetimos la suma 'b' veces
        resultado += abs(a)  # Sumamos 'a' en cada iteración
    
    # Ajustamos el signo si uno de los números es negativo
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        resultado = -resultado
    
    return resultado

# Ejemplo de uso
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print("Resultado:", multiplicar_con_sumas(num1, num2))