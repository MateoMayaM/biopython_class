'''
NAME
       Proogramacion_orientada_a_objetos

VERSION
        [1.#]

AUTHOR
        Mateo Maya Martínez <matteo.mayam@outlook.com>

DESCRIPTION
        Ejemplo de clase para describir a un jugador de futbol.

CATEGORY
       POO.

LIGA DE GITHUB: [https://github.com/MateoMayaM/python_class/blob/master/pythonII/tareas/Programacion_orientada_a_objetos]

'''


class futbolista ():
    def __init__(self, nombre, numero, posicion):
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion


class portero(futbolista):

    def __init__(self, nombre, numero, posicion):
        super().__init__(nombre, numero, posicion)
        self.posicion = "portero"

    def atajar(self):
        pass

class defensa(futbolista):

    def __init__(self, nombre, numero, posicion):
        super().__init__(nombre, numero, posicion)
        self.posicion= "defensa"

    def despejar(self):
        pass


class medio(futbolista):

    def __init__(self, nombre, numero, posicion):
        super().__init__(nombre, numero, posicion)
        self.posicion = "medio"


    def filtrar(self):
        pass

class delantero(futbolista):

    def __init__(self, nombre, numero, posicion):
        super().__init__(nombre, numero, posicion)
        self.posicion = "delantero"

    def metergol(self):
        pass

jugador = futbolista("Herrera", "14", "medio")
print(jugador.__dict__)

jugador2 = defensa ("Herrera", "8", "")
print(jugador2.__dict__)

jugador3 = delantero ("David", "10", "")
print(jugador3.__dict__)

