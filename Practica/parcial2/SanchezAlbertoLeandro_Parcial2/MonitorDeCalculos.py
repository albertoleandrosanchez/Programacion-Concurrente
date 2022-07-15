import threading

class MonitorDeCalculos():
    
    # count: Es una variable de tipo entero que representa el número de hilos que están esperando para leer/escribir.
    count = 0 
    # result: Es una variable de tipo entero que representa el resultado de la suma de las variables A y B.
    result = 0 
    # a: Es una variable de tipo entero que representa el valor de la variable A.
    a = 0  
    # b: Es una variable de tipo entero que representa el valor de la variable B.
    b = 0 

    # Inicializo el lock
    lock  = threading.RLock() 
    # Se crean los condicionales.
    generadorConditionLock = threading.Condition(lock)
    procesadorConditionLock = threading.Condition(lock)

    
    def __init__(self,quantity):
        self.limit = quantity

    # assign es una funcion que recibe 2 valores por parametro.
    # primero toma el lock.
    # si el contador count es menor a la variable limit, los generadores se duermen.
    # luego se asigna un nuevo valor a las variables de monitor, a y b.
    # luego se despierta a los procesadores.
    # finalmente libera el lock.
    def assign(self,valueA,valueB):
        self.lock.acquire()
        try:
            while(self.count < self.limit):
                self.generadorConditionLock.wait()
            self.count = 0
            self.a = valueA 
            self.b = valueB 
            self.procesadorConditionLock.notify_all()
        finally:
            self.lock.release()


    # substract a diferencia de assign no recibe parametros.
    # primero toma el lock.
    # si el contador count es igual a la variable limit, los procesadores se duermen.
    # luego se calcula el resultado de la suma de las variables A y B y se la asigna a la variable result.
    # luego se despierta a los generadores.
    # se retorna el resultado.
    # finalmente libera el lock.
    def substract(self):
        self.lock.acquire()
        try:
            while(self.count == self.limit):
                self.procesadorConditionLock.wait()
            self.result = self.a + self.b
            self.count += 1
            self.generadorConditionLock.notify_all()
            return self.result
        finally:
            self.lock.release()
