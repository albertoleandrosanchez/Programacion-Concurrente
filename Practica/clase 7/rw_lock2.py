""" rwlock.py
    Clase para implementar read-write locks sobre la libreria standard threading.
    rLock: Read Lock, permite multiples accesos concurrentes a operaciones de Lectura (Read)
    wLock: Write Lock, permite un unico acceso (exclusión mútuo) para Escritura (Write)
    Esto esta implementado con dos MUTEX (instancias threading.Lock) y una variable entera (num_r) que lleva
    la cuenta de la cantidad de Readers bloqueados. Un Lock (num_r_lock) protege el acceso a num_r y solo es
    utlizado por los Readers. El otro Lock (w_lock) es de acceso global y asegura la exclusión mutua de los
    writers. Esto requiere que un Lock adquirido por una thread pueda ser liberado por otra.

    Comenzar Lectura (adquirir Read Lock)
    1 obtener num_r_lock
    2 incrementar num_r
    3 Si num_r = 1, obtener w_lock
    4 liberar num_r_lock

    Fin de Lectura (Liberar Read Lock)
    1 obtener num_r_lock
    2 decrementar num_r
    3 Si num_r = 0, liberar w_lock
    4 liberar num_r_lock

    Comenzar Escritura
    1 obtener w_lock

    Fin de Escritura
    2 liberar w_lock

    Esta es una implementación de RW Locks con Preferencia de Lectura (Read-Preferring RW locks).
    Este tipo de RW lock permite la máxima concurrencia, pero pueden provocar falta de escritura (Write-Starvation)
    si la concurerncia es alta.
    Esto se debe a que los hilos writer no pueden adquirir el Lock mientras al menos un hilo reader lo tenga.
    Dado que varios hilos reader pueden tener el lock a la vez, un hilo writer puede quedarse esperando el lock
    mientras nuevos hilos reader pueden obtenerlo, incluso hasta el punto en que el writer tenga que esperar
    hasta que todos los readers que tienen el lock lo liberen.

    Nota: Hay otras implementaciones de RW Locks:

        Write-preferring RW Locks (resuelve el problema de writer-starvation)
        Unspecified-priority RW Locks

"""


# _______________________________________________________________________
# Imports

import logging
import random
from threading  import Lock, Thread
from time import time

# _______________________________________________________________________
# Class

class RWLock(object):
    """ Clase RWLock;  tiene como propósito permitir que un objeto sea leido por multiples hilos
        simultáneamente, pero solo puede ser escrito por un solo hilo a la vez.

        Uso:
            from rwlock import RWLock
            mi_RWLock = RWLock()

            # Al leer de mi_objeto
            mi_RWLock.r_acquire()
            try:
                # tareas de SOLO Lectura con mi_objeto
            finally:
                mi_RWLock.r_release()


            # Al escribir en my_obj:
            mi_RWLock.w_acquire()
            try:
                # tareas de escritura en mi_objeto
            finally:
                mi_RWLock.w_release()

    """
    # Constructor

    def __init__(self):

        self.w_lock = Lock()
        self.num_r_lock = Lock()
        self.num_r = 0

    # ___________________________________________________________________
    # Metodos de Lectura (Reading).

    def r_acquire(self):
        self.num_r_lock.acquire()
        self.num_r += 1
        if self.num_r == 1:
            self.w_lock.acquire()
        self.num_r_lock.release()

    def r_release(self):
        assert self.num_r > 0
        self.num_r_lock.acquire()
        self.num_r -= 1
        if self.num_r == 0:
            self.w_lock.release()
        self.num_r_lock.release()


    # ___________________________________________________________________
    # Métodos de Escritura (Writing).

    def w_acquire(self):
        self.w_lock.acquire()

    def w_release(self):
        self.w_lock.release()


rwlock = RWLock()
partido = ["",0,"",0] 
equipos = ["Boca", "River", "Racing", "Independiente", "San Lorenzo", "Huracán", "Gimnasia", 
"Estudiantes", "Velez", "Ferro", "Lanus", "Quilmes"]
def escritor(id):
    global partido
    global equipos
    nombreHilo= f"Escritor numero:{id}"
    while True:
        golesEquipo1= random.randint(0,3)
        golesEquipo2= random.randint(0,3)
        primerEquipo = equipos[random.randint(0,len(equipos)-1)]
        segundoEquipo = equipos[random.randint(0,len(equipos)-1)]
        while primerEquipo == segundoEquipo:
            segundoEquipo = equipos[random.randint(0,len(equipos)-1)]
        rwlock.w_acquire()
        try:
            partido[0] = primerEquipo
            partido[1] = golesEquipo1
            partido[2] = segundoEquipo
            partido[3] = golesEquipo2
            logging.info(f"Partido actualizado por {nombreHilo}")
        finally:
            rwlock.w_release()
            time.sleep(random.randint(1,2))
def lector(id):
    global partido
    global equipos
    nombreHilo= f'Lector-{id}:'
    while True:
        rwlock.r_acquire()
        try:
            logging.info(f"{nombreHilo} el resultado ue: {partido[0]}: {partido[1]} - {partido[2]}: {partido[4]}")
        finally:
            rwlock.r_release()
            time.sleep(random.randint(1,2))


class main():
    hilos = []
    for i in range(1):
        logging.info(f"Creando hilo escritor {i}")
        writer = Thread(target=escritor, args=(i))
        writer.start()
        hilos.append(writer)
    for r in range(4):
        logging.info(f"Creando hilo lector {r}")
        reader = Thread(target=lector, args=(r))
        reader.start()
        hilos.append(reader)
    for hilo in hilos:
        hilo.join()

if __name__ == '__main__':
    main()

