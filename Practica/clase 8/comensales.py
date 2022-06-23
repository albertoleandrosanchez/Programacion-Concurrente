import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Cocinero(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = 'Cocinero'

    def run(self):
        global platosDisponibles
        while (True):
            cocineroLock.acquire()
            logging.info('Reponiendo los platos...')
            platosDisponibles = 3
            platos.release(3)


class Comensal(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Comensal {numero}'

    def run(self):
        global platosDisponibles
        platos.acquire()
        platosDisponibles -= 1
        if( platosDisponibles == 0):
            cocineroLock.release()
        logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')

platosDisponibles = 3
platos = threading.Semaphore(3)
cocineroLock = threading.Lock()
Cocinero().start()

for i in range(20):
    Comensal(i).start()