import threading
import time
import random
import logging
from regionCondicional import *

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class RecursoFilosofo(Recurso):
    tenedor = threading.Lock()
    hayTenedorIzquierdo = True
    hayTenedorDerecho = True

recursoFilosofo = RecursoFilosofo()
def condicionTenedorIzquierdo():
    return recursoFilosofo.hayTenedorIzquierdo == True

def condicionTenedorDerecho():
    return recursoFilosofo.hayTenedorDerecho == True

regionTenedorIzquierdo = RegionCondicional(recursoFilosofo, condicionTenedorIzquierdo)
regionTenedorDerecho = RegionCondicional(recursoFilosofo, condicionTenedorDerecho)

@regionTenedorIzquierdo.condicion
def tomarTenedorIzquierdo():
    recursoFilosofo.tenedor.acquire()
    recursoFilosofo.hayTenedorIzquierdo = False

@regionTenedorDerecho.condicion
def tomarTenedorDerecho():
    recursoFilosofo.tenedor.acquire()
    recursoFilosofo.hayTenedorDerecho = False

class Filosofo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.name = nombre
        logging.info(f'Filósofo {self.name} se sentó en la mesa')

    def run(self):
        logging.info(f'Filósofo {self.name} comenzó a Pensar')
        while True:
            time.sleep(random.randint(1,5))
            logging.info(f'Filósofo {self.name} terminó de pensar {threading.current_thread()}')
            self.tomarTenedor()
            logging.info(f'Filósofo {self.name} termino de comer')
            time.sleep(random.randint(1))
            
    @RegionCondicional.condicion
    def tomarTenedor(self):
        if(self.condicion1()):
            RecursoFilosofo.condicion1 = False
            logging.info(f'Filósofo {self.name} obtuvo el tenedor Izquierdo {threading.current_thread()}')
            time.sleep(1)
            logging.info(f'Filósofo {self.name} liberó el tenedor Izquierdo {threading.current_thread()}')
            RecursoFilosofo.condicion1 = True
            if(self.condicion2()):
                RecursoFilosofo.condicion2 = False
                logging.info(f'Filósofo {self.name} los dos tenedores y esta comiendo {threading.current_thread()}')
                time.sleep(1)
                logging.info(f'Filósofo {self.name} liberó el tenedor Derecho {threading.current_thread()}')
                RecursoFilosofo.condicion1 = True
            else:
                logging.info(f'Filósofo {self.name} no esta disponible el tenedor derecho {threading.current_thread()}')    
        else:
            logging.info(f'Filósofo {self.name} no esta disponibles tenedor izquierdo')
            

def main():
    threads = []
    nombres = ["Socrates", "Platón", "Aristóteles", "Locke", "Descartes"]

    for i in range(5):
        filosofo = Filosofo(nombres[i])
        threads.append(filosofo)
        filosofo.start()

    for i in threads:
        i.join()

if __name__=='__main__':
    main()