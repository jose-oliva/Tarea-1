class Stack:
    def __init__(self):
        # Inicializa la lista donde se almacenaran los elementos
        # Al iniciarse, el stack esta vacio
        self._elementos = []

    def apilar(self, elemento):
        # Añade un nuevo elemento al final de la lista
        self._elementos.append(elemento)

    def desapilar(self):
        # Verifica si la pila esta vacia
        # Si es el caso, lanza un error porque no se puede desapilar algo vacio
        if self.esta_vacia():
            raise IndexError("desapilar desde un stack vacio")
        # Si no esta vacio, elimina y retorna el ultimo elemento añadido
        return self._elementos.pop()

    def ver_tope(self):
        # Comprueba si el stack esta vacio
        if self.esta_vacia():
            raise IndexError("ver tope del stack vacio")
        # Retorna el ultimo elemento sin eliminarlo
        return self._elementos[-1]

    def esta_vacia(self):
        # Retorna True si el stack no tiene elementos
        # Detecta si la lista está vacia
        return len(self._elementos) == 0

    def tamano(self):
        # Retorna la cantidad de elementos
        return len(self._elementos)

    def __str__(self):
        # Representa el stack en forma de cadena para imprimir
        # Invierte la lista para mostrar el tope (ultimo elemento) al principio
        return "Stack(tope->base): " + str(self._elementos[::-1])