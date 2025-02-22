def multiplicar(a,b):  
    if b==0:
      return 
    if b>0:
      return a + multiplicar(a, b - 1 )
    return multiplicar(a,-b)
print(multiplicar(3, -4)) 