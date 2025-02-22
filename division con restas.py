def dividir_con_restas(dividendo, divisor):
    if divisor == 0:
        return "Error: No se puede dividir por cero"

    resultado = 0
    negativo = (dividendo < 0) ^ (divisor < 0)  # Determina si el resultado será negativo
    
    dividendo, divisor = abs(dividendo), abs(divisor)  # Trabajamos con valores absolutos

    while dividendo >= divisor:  # Restamos mientras el dividendo sea mayor o igual al divisor
        dividendo -= divisor
        resultado += 1

    return -resultado if negativo else resultado  # Ajustamos el signo del resultado

# Ejemplo de uso
num1 = int(input("Introduce el dividendo: "))
num2 = int(input("Introduce el divisor: "))
print("Resultado:", dividir_con_restas(num1, num2))
