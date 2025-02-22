def fibonacci (n):
    if n <= 0: 
       return[]
    if n == 1:
       return [0]
    if n== 2:
       return [0,1]
    secuencia= fibonacci (n-1)
    secuencia.append(secuencia[-1]+secuencia[-2])
    return secuencia
    
num=int(input("intoduce la cantidad de numeros de fibonacci deseas: "))
print(fibonacci(num))




