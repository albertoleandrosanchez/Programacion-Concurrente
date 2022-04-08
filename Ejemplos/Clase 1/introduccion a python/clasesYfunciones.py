import threading
import time
import logging

from definiciones import dormir
from definiciones import UnThread

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


logging.info('Creando thread desde una función')
threadFunc = threading.Thread(target=dormir, name='thread desde una función')

logging.info('Creando thread desde una clase')
threadObj = UnThread()

logging.info('Lanzando los threads')
threadFunc.start()
threadObj.start()