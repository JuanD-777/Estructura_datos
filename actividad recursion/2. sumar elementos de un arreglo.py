def suma_arreglo(arre):
    if not arre:

     return 0
    return arre[0] + suma_arreglo(arre[1:])

numeros =[1,2,3,4,5,6]
print(suma_arreglo(numeros))



