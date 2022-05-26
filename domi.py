import time
import threading #hilos para concurrencia
import logging

from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


def dormir():
  time.sleep(1) #duerme por 1 seg


contador = Contador()


# ejemplo clásico secuencial
contador.iniciar()

dormir()
dormir()

contador.finalizar()
contador.imprimir()


# ejemplo con threads
contador.iniciar()

t1 = threading.Thread(target=dormir)
t2 = threading.Thread(target=dormir)

t1.start()
t2.start()

contador.finalizar()
contador.imprimir()


# ejemplo con threads, pero esperando que terminen
contador.iniciar()

t1 = threading.Thread(target=dormir)
t2 = threading.Thread(target=dormir)

t1.start()
t2.start()


t1.join() #esperá a que termine el lanzamiento del hilo t1
t2.join()

contador.finalizar()
contador.imprimir()