numero = 5
def factorial (n:int)->int:
    if n==1 :
     return n
    return factorial (n-1)*n

print(factorial(5))