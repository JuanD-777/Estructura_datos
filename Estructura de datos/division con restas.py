def dividir_con_restas(dividendo, divisor):
    if divisor == 0:
        return "Error: No se puede dividir por cero"

    resultado = 0  
    negativo = (dividendo < 0) ^ (divisor < 0)  
    
    dividendo, divisor = abs(dividendo), abs(divisor)  

    while dividendo >= divisor:  
        dividendo -= divisor
        resultado += 1

    return -resultado if negativo else resultado  


num1 = int(input("Introduce el dividendo: "))
num2 = int(input("Introduce el divisor: "))
print("Resultado:", dividir_con_restas(num1, num2))
