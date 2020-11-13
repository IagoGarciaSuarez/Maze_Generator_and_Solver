class Nodo:
    def __init__(self, id, costo, estado, padre, accion, p, f, objetivo):
        self.id = id
        self.costo = estado.celda.value
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.p = p
        self.f = f
        self.h = self.calcularHeuristica(objetivo)        
    
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
    
    def calcularHeuristica(self, objetivo):
        h = abs(self.estado.celda.posicion[0] - objetivo[0]) + abs(self.estado.celda.posicion[1] + objetivo[1])
        return h


    def calcularValor(self, estrategia, n):
        '''
        Función encargada de retornar un valor de f en función del nodo y la estrategia elegidas.
        '''
        if estrategia == 1:
            return 1/(n.p + 1)
        elif estrategia == 2:
            return n.p
        elif estrategia == 3:
            return n.costo
        elif estrategia == 4:
            return n.h
        elif estrategia == 5:
            return n.h + n.cost