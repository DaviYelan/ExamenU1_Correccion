from controls.expresion_aritmetica import evaluar_expresion

def registrar_expresion(expresion):
    try:
        resultado = evaluar_expresion(expresion)
        return {"expresion": expresion, "resultado": resultado}
    except Exception as e:
        print(f"Error: {e}")
        return None