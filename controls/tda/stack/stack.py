from controls.tda.stack.stackOperation import StackOperation

class Pila():
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        return self.elementos.pop()

    def peek(self):
        return self.elementos[-1]

    def is_empty(self):
        return len(self.elementos) == 0
    