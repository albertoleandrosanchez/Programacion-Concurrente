import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = 0

def hiloAFunc():
    global x
    x = random.randint(1, 100)
    logging.info(f'Soy {threading.current_thread().name} y el valor de x arrancó {x}')
    while(x != 0):
        x -= 1
        time.sleep(random.randint(0,1))
    logging.info(f'Soy {threading.current_thread().name} y el valor de x terminó {x}')

def hiloBFunc():
 
    global x
    logging.info(f'Soy {threading.current_thread().name} y el valor de x es {x}')
    while(x != 0):
        logging.info(f'El valor de x es {x}')
        time.sleep(random.randint(1,4))


def main():
    threadA = threading.Thread(target=hiloAFunc)
    threadB = threading.Thread(target=hiloBFunc)

    threadA.start()
    threadB.start()

    threadA.join()
    threadB.join()

if __name__ == '__main__':
    main()