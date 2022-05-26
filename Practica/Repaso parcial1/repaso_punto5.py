import random
import threading
import time
import logging


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = 0
mutex = threading.Lock()

def hiloAFunc():
    global x
    logging.info(f'Soy {threading.current_thread().name} y el valor de x arrancó {x}')
    while(x != 1000000):
        # conviene siempre liberarlo al toque
        x += 1
        time.sleep(1)
    logging.info(f'Soy {threading.current_thread().name} y el valor de x terminó {x}')

def hiloBFunc():
    global x
    while(True):
        logging.info(f'Soy {threading.current_thread().name} y el valor de x es {x}')
        time.sleep(2)


def main():
    threadA = threading.Thread(target=hiloAFunc)
    threadB = threading.Thread(target=hiloBFunc)

    threadA.start()
    threadB.start()

    threadA.join()
    threadB.join()

if __name__ == '__main__':
    main()