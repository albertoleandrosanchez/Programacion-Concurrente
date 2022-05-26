
class ColaFIFO:

    def __init__(self):
        self.elementos = []

    def insertar(self, dato):
        self.elementos.append(dato)
        return dato

    def extraer(self):
        return self.elementos.pop(0)

    def ultimo(self):
        return self.elementos[-1]

    def primero(self):
        return self.elementos[0]

    def cola_vacia(self):
        return len(self.elementos) == 0

    def cantidad_elementos(self):
        return len(self.elementos)


def main():
    cola = ColaFIFO()

    # check if esta_vacia()

    print(cola.cola_vacia())

    for i in range (1,6):
        cola.insertar(i)

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

    print(cola.primero(),cola.ultimo())
    cola.extraer()
    print(cola.primero(),cola.ultimo())


    cola.extraer()
    cola.extraer()
    cola.extraer()
    cola.extraer()

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

if __name__ == '__main__':
    main()
