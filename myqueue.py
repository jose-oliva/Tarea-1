class Queue:
    def __init__(self):
        # Crea la lista
        self._elementos = []

    def encolar(self, elemento):
        # Agrega un elemento al final de la lista
        self._elementos.append(elemento)

    def desencolar(self):
        # Verifica si la cola esta vacia
        # Si es el caso, lanza un error
        if self.esta_vacia():
            raise IndexError("desencolar desde una cola vacia")
        # Sino está vacia, elimina y retorna el primer elemento de la lista
        return self._elementos.pop(0)

    def ver_frente(self):
        # Comprueba que la cola no este vacia
        if self.esta_vacia():
            raise IndexError("ver frente en una cola vacia")
        # Retorna el primer elemento sin eliminarlo
        return self._elementos[0]

    def esta_vacia(self):
        # Retorna True si la cola no tiene elementos
        return len(self._elementos) == 0

    def tamaño(self):
        # Retorna el numero de elementos
        return len(self._elementos)

    def __str__(self):
        # Devuelve una representacion de la cola
        return "Queue(frente->final): " + str(self._elementos)