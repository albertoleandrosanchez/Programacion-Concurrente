import logging
from MonitorDeCalculos import *
from Procesador import *
from Generador import *

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# Escriba un programa que ejecute los siguientes hilos que utilizan datos almacenados en dos variables de tipo entero A y B.

# Generador: ejecuta un bucle infinito en el cual asigna a las variables A y B valores enteros aleatorios entre 0 y 100 e imprimen en pantalla un mensaje identificando al hilo y el valor que le asignó a las variables. Por ejemplo:

# Thread-9 asignó A = 31 y B = 22

# Procesador: ejecuta un bucle infinito en el cual lee los valores de las variables, calcula la suma y la imprime en un mensaje que incluya la identificación del hilo. Por ejemplo:

# Thread-2 calculó A + B = 53



# Implementar la concurrencia del programa de modo que:

# Los hilos generadores deben esperar hasta que por lo menos uno y no más que tres Procesadores lea/n el valor de las variables.
# Los hilos Procesadores deben esperar a que algún generador asigne nuevos valores a las variables si los valores actuales ya fueron leídos por otros tres Procesadores.
# El hilo principal debe arrancar por lo menos 10 hilos de cada tipo (Generador y Procesador).

class ProductorGeneradorMain():
    # Creo una variable de tipo MonitorDeCalculos.

    bufferMonitorDeCalculos = MonitorDeCalculos(3)
    threads = []

    for i in range(0,10):
        # dado que se pedia 10 hilos de cada tipo, se crean 10 hilos de cada tipo.
        procesador = Procesador(bufferMonitorDeCalculos)
        generador = Generador(bufferMonitorDeCalculos)

        # Se crean los hilos.
        procesador.start()
        generador.start()
    
        # Se guardan los hilos en una lista.
        threads.append(procesador)
        threads.append(generador)   

    for i in threads:
        # Se espera a que los hilos terminen.
        i.join()


if __name__ == "__main__":
    ProductorGeneradorMain()
