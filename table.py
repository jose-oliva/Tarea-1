class TableHashDictionary:
    def __init__(self):
        # Crea un diccionario
        self._tabla = {}

    def asignar(self, clave, valor):
        # Si la clave ya existe, su valor sera reemplazado
        self._tabla[clave] = valor

    def obtener(self, clave):
        # Verifica que la clave exista
        if clave not in self._tabla:
            # Lanza error si la clave no esta presente
            raise KeyError(f"Clave '{clave}' no encontrada")
        # Retorna el valor asociado a la clave
        return self._tabla[clave]

    def eliminar(self, clave):
        # Elimina el par clave-valor si la clave existe
        # Si la clave no esta no hace nada
        if clave in self._tabla:
            del self._tabla[clave]

    def contiene(self, clave):
        # Retorna True si la clave esta en la tabla
        return clave in self._tabla

    def tamano(self):
        # Retorna el numero de pares clave-valor
        return len(self._tabla)

    def claves(self):
        # Devuelve una lista con todas las claves
        return list(self._tabla.keys())

    def valores(self):
        # Devuelve una lista con todos los valores
        return list(self._tabla.values())

    def __str__(self):
        # Retorna una representacion de la tabla para impresion
        return f"TablaHash: {self._tabla}"