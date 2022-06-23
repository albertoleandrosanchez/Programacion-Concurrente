import threading
import logging
import random
import time
from regionCondicional import *

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


class Recurso1(Recurso):
    dato1 = 0
    numLectores = 0
recurso = Recurso1()

def condicionLector():
    return True

def condicionEscritor():
    return recurso.numLectores == 0

regionLector = RegionCondicional(recurso, condicionLector)
regionEscritor = RegionCondicional(recurso, condicionEscritor)

@regionLector.condicion
def seccionCriticaLector():
    recurso.numLectores += 1
    time.sleep(1)
    recurso.numLectores -= 1

@regionEscritor.condicion
def seccionCriticaEscritor():
    recurso.dato1 = random.randint(0,100)
    logging.info(f'Escritor escribe dato1 = {recurso.dato1}')



def Lector():
    while True:
        logging.info(f'Lector lee dato1 = {recurso.dato1}')
        seccionCriticaLector()
        time.sleep(random.randint(3,6))

def Escritor():
    while True:
        seccionCriticaEscritor()
        time.sleep(random.randint(1,4))

def main():
    nlector = 10
    nescritor = 2

    for k in range(nlector):
        threading.Thread(target=Lector, daemon=True).start()

    for k in range(nescritor):
        threading.Thread(target=Escritor, daemon=True).start()

    time.sleep(300)


if __name__ == "__main__":
    main()

