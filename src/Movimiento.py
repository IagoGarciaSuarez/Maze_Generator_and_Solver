class Movimiento():
    def __init__(self, posicion, direccion):
        self.posicion = posicion
        self.direccion = direccion

    def diccionario(self):
        direcciones = {
            "N" : (0, 1),
            "E" : (1, 0),
            "S" : (0, -1),
            "O" : (-1, 0)
        }