import random
import threading
import time
import logging


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = random.randint(1, 100)
mutex = threading.Lock()

def hiloAFunc():
    global x
    logging.info(f'Soy {threading.current_thread().name} y el valor de x arrancó {x}')
    while(x != 0):
        mutex.acquire() 
        # conviene siempre liberarlo al toque
        x -= 1
        mutex.release()
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
    threadA2 = threading.Thread(target=hiloAFunc)
    threadB = threading.Thread(target=hiloBFunc)

    threadA.start()
    threadA2.start()
    threadB.start()

    threadA.join()
    threadA2.join()
    threadB.join()

if __name__ == '__main__':
    main()