# Modulo 3: Compiladores (Tarea #1)

# Jose Antonio Ramirez Oliva - A00830223

Se desarrollaron tres estructuras clasicas de datos: Stack, Queue y Tabla Hash en el lenguaje Python. Se prueban en un programa de test cases que valida el correcto funcionamiento de cada estructura. El objetivo de esta tarea fue entender como funcionan estas estructuras y explorar el diseno orientado a objetos para crearlas, en mi caso desde cero.

## Estructuras Implementadas

### Stack

Es una estructura que sigue la regla LIFO ("Last In First Out").

Operaciones principales:

- apilar(elemento): Anade un elemento al tope de la pila.
- desapilar(): Elimina y retorna el elemento en el tope.
- ver_tope(): Devuelve el elemento en el tope sin eliminarlo.
- esta_vacia(): Verifica si la pila esta vacia.
- tamano(): Retorna la cantidad de elementos presentes.

En la implementacion se utiliza una lista para almacenar los elementos, aprovechando la operacion append() para apilar y pop() para sacar.

### Queue

Es una estructura que sigue la regla FIFO ("First In First Out").

Operaciones principales:

- encolar(elemento): Anade un elemento al final de la cola.
- desencolar(): Elimina y retorna el elemento al frente de la cola.
- ver_frente(): Muestra el elemento al frente sin eliminarlo.
- esta_vacia(): Checa si la cola esta vacia.
- tamano(): Indica la cantidad de elementos en la cola.

De nuevo, se usa listas. Para desencolar se utiliza pop(); en aplicaciones mas complejas o que se quieran escalar se optaria por otras estructuras para evitar el coste computacional de desplazamiento.

### Tabla Hash

Simula el comportamiento de un diccionario.

Operaciones principales:

- asignar(clave, valor): Inserta o actualiza un par clave-valor.
- obtener(clave): Obtiene el valor asociado a una clave.
- eliminar(clave): Borra el par clave-valor correspondiente.
- contiene(clave): Verifica la existencia de una clave.
- tamano(), claves(), valores(): Metodos auxiliares para obtener informacion de la tabla.

Se utilizo el diccionario nativo de Python internamente para funcionalidad.

## Explicacion del Flujo del Programa de Pruebas

El archivo main.py contiene funciones para probar cada estructura por separado:

### Prueba de Stack:

- Se apilan tres valores, se imprime el contenido de la pila.
- Se inspecciona el tope con ver_tope().
- Se desapila un elemento y se muestra la estructura final.
- Se prueban los metodos tamano() y esta_vacia().

### Prueba de Queue:

- Se encolan tres elementos.
- Se inspecciona el frente con ver_frente().
- Se desencola un elemento y se muestra la estructura final.
- Se verifica con tamano() y esta_vacia().

### Prueba de Tabla Hash:

- Se asignan varias claves con valores.
- Se obtienen datos y se listan claves y valores.
- Se elimina un par y se valida la presencia con contiene().
- Se verifica tamano final.

El main las ejecuta en secuencia, imprimiendo los resultados en consola.
