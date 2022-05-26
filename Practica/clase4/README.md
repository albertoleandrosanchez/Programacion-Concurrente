# Condición de Sincronización - Ejercicios con Locks

## Cola FIFO compartida

El siguiente archivo python contiene la definición de la clase *ColaFIFO* que implementa una cola First In, First Out.
```
colaFIFO.py
```
El contenido de la cola se almacena en una atributo lista llamado “*elementos*”

La clase contiene 7 métodos

***Constructor*** : inicializa la lista “elementos” para el contenido de la cola

***insertar(dato)*** : inserta un elemento en la cola

***extraer(dato)*** extrae un elemento en la cola

***ultimo()*** : muestra el último elemento de la cola

***primero()*** : muestra el primer elemento de la cola (próximo a salir)

***cola_vacia()*** : devuelve Verdadero si la cola está vacia

***cantidad_elementos()*** : retorna la cantidad de elementos en la cola

El script incluye una función ***main()*** cuyo propósito es probar los métodos.

## Ejercicio

1. Leer y analizar que hace el código de este programa. 
**Analizar hasta comprender todas las líneas del código**

2. En un archivo python separado, importar la clase ColaFIFO, instanciar una cola de ésta clase y luego implementar un programa que ejecute las siguientes threads:

	 - Una thread (productor) que ejecute un loop infinito que en cada iteración inserte en la cola un valor numérico generado aleatoriamente (con valores entre 0 y 100), imprima un mensaje de logging indicando que se realizó la inserción y espere (sleep) dos segundos.
	
	  **Esta thread debe recibir como argumentos un objeto ColaFIFO y un valor numérico (retardo), inicialmente de 2 segundos.**
		  Por ejemplo:
      ````
        # a partir de una clase derivada de Thread
        c1 = Cons(cola, 2) 
      
        # directamente desde el módulo threading 
        c1 = threading.Thread(target=cons, args=(cola, 2))
      ````
  
   - Una thread (consumidor) que ejecute un loop infinito que en cada iteración extraiga un elemento de la cola, genere un mensaje de logging con el valor del elemento extraído y luego espere (sleep) dos segundos.  

	  **Esta thread debe recibir como argumentos un objeto ColaFIFO y un valor numérico (retardo), inicialmente de 2 segundos.**
    
    Ejemplos: 
    ```
      # a partir de una clase derivada de Thread
      p1 = Prod(cola, 2) 
     
      # directamente desde el módulo threading 
      p1 = threading.Thread(target=prod, args=(cola, 2))  
    ```

    **Preferentemente, implementar estas threads a partir de clases derivadas de Thread que reciban como argumento el objeto de clase ColaFIFO instanciado y el valor numérico de retardo, en vez de hacerlo directamente del módulo threading.**

    **Las threads deben permanecer ejecutándose indefinidamente, no debe terminar el programa después de lanzarlas. Coloque todo el código que sea necesario para esto.**

3. Ejecute el programa y analice los resultados. Obtiene en alguna de las ejecuciones datos inconsistentes o errores? En caso afirmativo, analice los resultados identificando las causas de las inconsistencias o errores.

4. Como modificaría la clase ***ColaFIFO*** de modo que su constructor reciba un argumento “size” que establezca el tamaño máximo (cantidad de elementos) de la cola, y modifique los métodos que sean necesarios para asegurar que la cantidad de elementos en la cola no supere esa cantidad de elementos.

5. Modifique el programa de modo de instanciar una nueva cola de tamaño (size) 10 y modifique los retardos de productor y consumidor de modo que queden los dos iguales (1 segundo).

6. Ejecute el programa y observe los resultados explicando lo que observa.
