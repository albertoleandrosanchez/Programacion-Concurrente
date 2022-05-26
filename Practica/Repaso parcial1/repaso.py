import random
import threading
import time
import logging
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def imprimir():
    tiempoDeInicio = time.perf_counter()
    logging.info(f'Arrancó {threading.current_thread().name}, somos {threading.active_count()} threads' )
    time.sleep(random.randint(1,5))
    tiempoDeFin = time.perf_counter()
    logging.info(f'Terminó {threading.current_thread().name}, somos {threading.active_count()} threads')
    logging.info(f'pasaron { tiempoDeFin - tiempoDeInicio} segundos')
if __name__ == '__main__':
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=imprimir))

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()