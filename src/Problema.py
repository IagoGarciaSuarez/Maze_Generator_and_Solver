from Laberinto import Laberinto
from Sucesores import Sucesores
from Estado import Estado

class Problema():
    def __init__(self, path, start):
        self.laberinto = Laberinto(True, path)
        self.sucesores = Sucesores()
        self.estado = Estado(self.laberinto[start[0]][start[1]])
        