from stack import Stack
from myqueue import Queue
from table import TableHashDictionary


def probar_stack():
    # Funcion para probar Stack
    print("Prueba de Stack")
    pila = Stack()

    # Apila tres valores
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)

    # Imprime el estado actual
    print(pila)

    # Muestra el elemento que esta en el tope
    print("Tope:", pila.ver_tope())

    # Desapila el elemento en el tope y lo imprime
    print("Desapilar:", pila.desapilar())

    # Muestra el stack después de desapilar un elemento
    print("Despues de desapilar:", pila)

    # Imprime la cantidad de elementos en el stack
    print("Tamaño:", pila.tamano())

    # Indica si el stack esta vacio
    print("¿Vacia?:", pila.esta_vacia())
    print()


def probar_queue():
    # Funcion para probar Queue
    print("Prueba de Queue")
    cola = Queue()

    # Encola tres elementos
    cola.encolar("A")
    cola.encolar("B")
    cola.encolar("C")

    # Imprime la fila
    print(cola)

    # Muestra el primer elemento
    print("Frente:", cola.ver_frente())

    # Desencola el primer elemento y lo imprime
    print("Desencolar:", cola.desencolar())

    # Muestra la queue despues de desencolar un elemento
    print("Despues de desencolar:", cola)

    # Imprime la cantidad de elementos
    print("Tamaño:", cola.tamano())

    # Indica si esta vacia
    print("¿Vacia?:", cola.esta_vacia())
    print()


def probar_tabla():
    # Funcion para probar Tabla Hash.
    print("Prueba de Tabla Hash")
    tabla = TableHashDictionary()

    # Asigna pares clave-valor
    tabla.asignar("nombre", "Jose")
    tabla.asignar("edad", 23)
    tabla.asignar("ciudad", "Monterrey")

    # Imprime la tabla
    print(tabla)

    # Muestra el valor asociado con la clave "nombre".
    print("Obtener 'nombre':", tabla.obtener("nombre"))

    # Imprime claves actuales
    print("Claves:", tabla.claves())

    # Imprime valores actuales
    print("Valores:", tabla.valores())

    # Elimina el par con clave "edad"
    tabla.eliminar("edad")

    # Muestra la tabla al eliminar la clave "edad"
    print("Despues de eliminar 'edad':", tabla)

    # Verifica si la clave "ciudad" esta
    print("¿Contiene 'ciudad'?:", tabla.contiene("ciudad"))

    # Imprime la cantidad actual de pares
    print("Tamaño:", tabla.tamano())
    print()


if __name__ == "__main__":
    # Ejecuta las pruebas
    probar_stack()
    probar_queue()
    probar_tabla()