from Direcciones import Direcciones
from Estado import Estado

class Sucesores():
    def sucesores(self, nodo, laberinto, costo = 1):
        sucList = []
        cell = nodo.estado.celda
        f, c = cell.posicion[0], cell.posicion[1]
        if cell.norte:
            vDir = Direcciones.valorDir["N"]
            fN = f + vDir[0]
            cN = c + vDir[1]
            vecino_N = laberinto.getCelda((fN,cN))
            sucList.append(("N", vecino_N, vecino_N.value + costo))

        if cell.este:
            vDir = Direcciones.valorDir["E"]
            fE = f + vDir[0]
            cE = c + vDir[1]
            vecino_E = laberinto.getCelda((fE,cE))
            sucList.append(("E", vecino_E, vecino_E.value + costo))

        if cell.sur:
            vDir = Direcciones.valorDir["S"]
            fS = f + vDir[0]
            cS = c + vDir[1]
            vecino_S = laberinto.getCelda((fS,cS))
            sucList.append(("S", vecino_S, vecino_S.value + costo))

        if cell.oeste:
            vDir = Direcciones.valorDir["O"]
            fO = f + vDir[0]
            cO = c + vDir[1]
            vecino_O = laberinto.getCelda((fO,cO))
            sucList.append(("O", vecino_O, vecino_O.value + costo))

        return sucList
    