# Repaso Primer Parcial

## Ejercicios:

1. Implemente un programa que ejecute 10 hilos que impriman un mensaje identificando al hilo, luego esperen un tiempo aleatorio entre 1 y 5 segundos y luego impriman un mensaje indicando que terminaron (identificando al hilo)
2. Modifique el programa anterior de modo que pueda medir e imprimir el tiempo total que tomo ejecutarse cada hilo (en milisengundos)
3. Implemente un programa que tenga dos hilos A y B, los dos con acceso a una variable X. El hilo A inicializa la variable en un valor entero aleatorio (entre 1 y 100) y lo decrementa en 1 hasta llegar a 0 intercalando un retardo aleatorio entre 0 y 1 segundo entre cada decremento de X. El hilo B hará iteraciones cada un tiempo aleatorio entre 1 y 4 segundos, imprimiendo el valor de X en cada iteración hasta que X sea 0. Tanto A como B deberan imprimir mensajes al arrancar y al terminar, identificando al hilo. El hilo A deberá también indicar el valor inicial de X en el mensaje de arranque o final. Pregunta: Hay condiciones de carrera? Como las evitaria?
4. Modificar el programa anterior para que se ejecuten 2 hilos A y un hilo B. Identificar (con comentarios) las zonas críticas y colocar los objetos necesarios para evitar condiciones de carrera.
5. Implemente un programa que pueda lanzar 10 hilos tipo A y 2 hilos tipo B, todos con acceso a una variable global X incializada en 0. Hilos A incrementan el valor de X hasta 1000000. Hilo B imprime el valor de X cada 2 segundos. Colocar líeas de comentario en el código, identificando las zonas críticas y los objetos utilizados para evitar condiciones de carrera.



<sub>[Daniel Buaon - unahur-progra-concu-1-2021](https://github.com/unahur-progra-concu-1-2021)</sub>