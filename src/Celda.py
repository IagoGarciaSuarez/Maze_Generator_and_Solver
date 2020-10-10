class Celda():
    def __init__(self, norte, este, sur, oeste, id=0):
        self.norte = norte
        self.este = este
        self.sur = sur
        self.oeste = oeste
        self.visitada = False

        