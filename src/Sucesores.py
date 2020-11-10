from Direcciones import Direcciones
from Estado import Estado

class Sucesores():
    def sucesores(self, nodo, laberinto, costo = 1):
        sucList = []
        cell = nodo.celda
        f, c = cell.posicion[0], cell.posicion[1]
        if cell.norte:
            vDir = Direcciones.valorDir["N"]
            f += vDir[0]
            c += vDir[1]
            vecino_N = laberinto[f][c]
            sucList.append(("N", Estado(cell), costo))
        if cell.este:
            vDir = Direcciones.valorDir["E"]
            f += vDir[0]
            c += vDir[1]
            vecino_E = laberinto[f][c]
            sucList.append(("E", Estado(cell), costo))
        if cell.sur:
            vDir = Direcciones.valorDir["S"]
            f += vDir[0]
            c += vDir[1]
            vecino_S = laberinto[f][c]
            sucList.append(("S", Estado(cell), costo))
        if cell.oeste:
            vDir = Direcciones.valorDir["O"]
            f += vDir[0]
            c += vDir[1]
            vecino_O = laberinto[f][c]
            sucList.append(("O", Estado(cell), costo))
    