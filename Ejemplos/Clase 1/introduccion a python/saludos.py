import logging



def saludar(quien):
  # interpolación de string
  logging.info(f'hola {quien} ¿cómo estás hoy?')
  


class Recepcionista:
  # constructor
  def __init__(self, titulo):
    # atributo o variable de instancia
    self.titulo = titulo

  # método, siempre va self como primer parámetro
  def saludar(self, quien):
    logging.info(self.armarMensajito(quien))

  def armarMensajito(self, quien):
    return f'hola {self.titulo} {quien} ¿cómo estás hoy?'


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# acá estoy creando un objeto nuevo
fernando = Recepcionista('Sr./a')

# acá estoy llamando a un método, notar que no paso dos argumentos
# el self es mágico
fernando.saludar('nicolás')
fernando.saludar('uma')

saludar('fede')
saludar('amanda')


