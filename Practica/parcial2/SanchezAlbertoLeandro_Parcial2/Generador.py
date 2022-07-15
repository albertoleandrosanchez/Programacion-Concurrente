import logging
import random
import threading
import time 

# Creamos la Clase generador. Que es muy parecida a la clase Procesador

class Generador(threading.Thread):
      # La clase Gemerador recibe como parametro un buffer de tipo MonitorDeCalculos.
    def __init__(self, bufferMonitorDeCalculos):
        super().__init__()
        # este buffer se lo asignamos a la varaible buffer de la clase Generador.
        self.buffer = bufferMonitorDeCalculos
        
    # El metodo run es el que se ejecuta cuando se crea un nuevo hilo.
    def run(self):
        while(True):
            # Se generan dos valores aleatorios.
            # Se asignan a las variables A y B.
            # Se llama a la funcion assign de la clase MonitorDeCalculos.
            # Se imprime en pantalla el valor de A y B.
            valueA = random.randint(0,100)
            valueB = random.randint(0,100)
            self.buffer.assign(valueA,valueB)
            logging.info(f'{threading.current_thread().getName()} asignó A = {valueA} y B = {valueB}')
            time.sleep(5)
