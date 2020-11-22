class Celda():
    def __init__(self, vecinos, posicion, value = 0):
        self.value = value
        self.norte = vecinos[0]
        self.este = vecinos[1]
        self.sur = vecinos[2]
        self.oeste = vecinos[3]
        self.posicion = posicion
        self.visitada = False

    def __str__(self):
        return ''.join(str(self.posicion))

    def __repr__(self):
        return self.__str__()
        
    def getValue():
        return self.value