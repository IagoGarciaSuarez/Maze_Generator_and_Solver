class Nodo:
    def __init__(self, id, costo, estado, padre, accion, p, f):
        self.id = id
        self.costo = costo
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.p = p
        self.f = f
        self.h = self.calcularHeuristica()
    
    def crearListaNodosSuc(self, frontera, sucList, nodoActual, prof_max, estrategia):
        if nodoActual.p < prof_max:
            listaSuc = []
            for suc in sucList:
                accion, estado, costo = suc
                nodoSuc = Nodo(frontera.next_id, nodoActual.costo + costo, estado, nodoActual, accion, nodoActual.p + 1, None)
                nodoSuc.f = self.calcularValor(estrategia, nodoSuc)
                listaSuc.append(nodoSuc)
                frontera.next_id += 1

            return listaSuc
    
    def calcularHeuristica(self):
        return self.h

    def calcularValor(self, estrategia, n):
        return self.f