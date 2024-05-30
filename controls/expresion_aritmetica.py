from controls.tda.stack.stack import Pila
from models.operadores import operadores

def evaluar_expresion(expresion):
    
    pila = Pila()

    for elemento in expresion.split():
        if elemento in operadores:
            if pila.is_empty() or pila.peek() in operadores:
                raise ValueError("Error de sintaxis")
            op2 = pila.pop()
            op1 = pila.pop()
            if elemento == '+':
                resultado = op1 + op2
            elif elemento == '-':
                resultado = op1 - op2
            elif elemento == '*':
                resultado = op1 * op2
            elif elemento == '/':
                if op2 == 0:
                    raise ZeroDivisionError("División por cero")
                resultado = op1 / op2
            elif elemento == '^':
                resultado = op1 ** op2
            pila.push(resultado)
        else:
            pila.push(float(elemento))

    if pila.is_empty() or len(pila.elementos) > 1:
        raise ValueError("Error de sintaxis")
    return pila.pop()