class Estado():
    def __init__(self, celda):
        self.celda = celda
        self.id = (celda.posicion[0], celda.posicion[1])

    def __str__(self):
        return ''.join(str(self.id))

    def __repr__(self):
        return self.__str__()