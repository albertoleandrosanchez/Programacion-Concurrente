import threading
import logging
import random
import time
from regionCondicional import *

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


class Recurso1(Recurso):
    dato1 = 0
    numEscritores = 0
    escritorPide = True
recurso = Recurso1()

def condicionLector():
    return recurso.numEscritores == 0

def condicionEscritor():
    return True
    

regionLector = RegionCondicional(recurso, condicionLector)
regionEscritor = RegionCondicional(recurso, condicionEscritor)

@regionLector.condicion
def seccionCriticaLector():
    logging.info(f'Lector lee dato1 = {recurso.dato1}')
    time.sleep(1)

@regionEscritor.condicion
def seccionCriticaEscritor():
    recurso.dato1 = random.randint(0,100)
    logging.info(f'Escritor escribe dato1 = {recurso.dato1}')



def Lector():
    while True:
        seccionCriticaLector()
        time.sleep(random.randint(3,6))

def Escritor():
    while True:
        recurso.numEscritores += 1
        seccionCriticaEscritor()
        recurso.numEscritores -= 1
        time.sleep(random.randint(1,4))


def main():
    nlector = 10
    nescritor = 2
    for k in range(nescritor):
        threading.Thread(target=Escritor, daemon=True).start()

    for k in range(nlector):
        threading.Thread(target=Lector, daemon=True).start()


    time.sleep(300)


if __name__ == "__main__":
    main()

