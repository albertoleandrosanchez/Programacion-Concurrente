import threading
import logging
import time
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


# Escriba un programa que ejecute los siguientes hilos que utilizan datos almacenados en dos variables de tipo entero A y B.

# Generador: ejecuta un bucle infinito en el cual asigna a las variables A y B valores enteros aleatorios entre 0 y 100 e imprimen en pantalla un mensaje identificando 
# al hilo y el valor que le asignÃ³ a las variables. Por ejemplo:

# Thread-9 asignÃ³ A = 31 y B = 22

# Procesador: ejecuta un bucle infinito en el cual lee los valores de las variables, calcula la suma y la imprime en un mensaje que incluya la identificaciÃ³n del hilo. 
# Por ejemplo:

# Thread-2 calculÃ³ A + B = 53

# Implementar la concurrencia del programa de modo que:

# Los hilos generadores deben esperar hasta que por lo menos uno y no mÃ¡s que dos Procesadores lea/n el valor de las variables.

# Los hilos Procesadores deben esperar a que algÃºn generador asigne nuevos valores a las variables si los valores actuales ya fueron leÃ­dos por otros dos Procesadores.

# El hilo principal debe arrancar por lo menos 10 hilos de cada tipo (Generador y Procesador).

class MonitorAB():
    A = 0
    B = 0
    lock = threading.RLock()
    
    leido = threading.Condition(lock)
    escrito = threading.Condition(lock)

    def __init__(self):
        super().__init__()
        self.fueLeido = True

    def generarValor(self):
        self.lock.acquire()
        try:
            while(not self.fueLeido):
                self.leido.wait()     
            self.A = random.randint(0,100)
            self.B = random.randint(0,100)
            self.fueLeido = False
            self.escrito.notify_all()
        finally:
            self.lock.release()
            logging.info(f'{threading.current_thread().name} A: {self.A} B: {self.B}')


    def obtenerSuma(self):
        self.lock.acquire()
        try:
            while(self.fueLeido):
                self.escrito.wait()
            self.fueLeido = True
            self.leido.notify_all()
        finally:
            self.lock.release()
            return (self.A + self.B)


class hiloGenerador(threading.Thread):
    def __init__(self, recursoAB):
        super().__init__()
        self.recurso = recursoAB


    def run(self):
        while True:
            self.recurso.generarValor()
            time.sleep(random.randint(0,3))

class hiloProcesador(threading.Thread):
    def __init__(self, recursoAB):
        super().__init__()
        self.recurso = recursoAB


    def run(self):
        while True:
            suma = self.recurso.obtenerSuma()
            logging.info(f'{threading.current_thread().name} Suma = {suma}')
            time.sleep(random.randint(0,3))

def funcionPrincipal():
    recursoAB = MonitorAB()
    hilos = []

    for i in range(5):
        gen = hiloGenerador(recursoAB)
        proc = hiloProcesador(recursoAB)
        gen.start()
        proc.start()
        hilos.append(gen)
        hilos.append(proc)

    for i in hilos:
        i.join()


if __name__ == "__main__":
    funcionPrincipal()