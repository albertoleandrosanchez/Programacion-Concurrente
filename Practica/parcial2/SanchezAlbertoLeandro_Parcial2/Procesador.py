import logging
import threading
import time

class Procesador(threading.Thread):
    # La clase Procesador recibe como parametro un buffer de tipo MonitorDeCalculos.
    def __init__(self,bufferMonitorDeCalculos):
        super().__init__()
        # este buffer se lo asignamos a la varaible buffer de la clase Procesador.
        self.buffer = bufferMonitorDeCalculos

    # El metodo run es el que se ejecuta cuando se crea un nuevo hilo.
    # este metodo se encarga de realizar la suma de las variables A y B.
    # y retornar el resultado en un logging.info.
    def run(self):
        while(True):
            # Se llama a la funcion substract de la clase MonitorDeCalculos.
            # Se imprime en pantalla el valor de A y B.
            # Se retorna el resultado de la suma en un logging.info.
            valor = self.buffer.substract()
            logging.info(f'{threading.current_thread().getName() } calculó A + B = {valor}') 
            time.sleep(5)

