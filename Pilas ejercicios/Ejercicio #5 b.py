# Crear un programa que verifique si una expresión mediante simbolos está balanceada.                                  
class VerificadorBalanceo:
    def __init__(self, expresion):
        self.expresion = expresion
        self.pila = []
        self.pares = {')': '(', '}': '{', ']': '['}

# Método para verificar si la expresión está balanceada
    def verificar_balanceo(self):
        for caracter in self.expresion:
            if caracter in '({[':
                self.pila.append(caracter)
            elif caracter in ')}]':
                if not self.pila or self.pila.pop() != self.pares[caracter]:
                    return False
        return not self.pila
    
    def __str__(self):
        return f'La expresión {self.expresion} está balanceada: {self.verificar_balanceo()}'    
    
# Ejemplo de uso 
expresion1 = VerificadorBalanceo('[{()}]')
print(expresion1)
expresion2 = VerificadorBalanceo(']')
print(expresion2)


