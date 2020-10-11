class Celda():
    def __init__(self, norte, este, sur, oeste, posicion, value=0):
        self.norte = norte
        self.este = este
        self.sur = sur
        self.oeste = oeste
        self.posicion = posicion
        self.value = value
        self.visitada = False

    def __str__(self):
        return ''.join(str(self.posicion))

    def __repr__(self):
        return self.__str__()