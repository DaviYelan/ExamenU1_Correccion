def listar_expresiones(expresiones):
    print("Expresiones registradas:")
    for expresion in expresiones:
        print(f"{expresion['expresion']} = {expresion['resultado']}")