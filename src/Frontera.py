from heapq import heappop, heappush

class Frontera:
    '''
    Esta clase contiene nuestra Frontera.
    Los distintos atributos que tendrá son:
        - Frontera.frontera: el array de la frontera
        - Frontera.next_id: el id del próximo nodo que generemos
    '''
    def __init__(self):
        self.frontera = []
        self.next_id = 0

    def insertar_nodo(self, nodo):
        '''
        Función que introducirá en un nodo en la frontera usando una Priority Queue, ordenada primeramente en función del
        valor de la f del nodo, y después por el id del nodo
        '''
        heappush(self.frontera, (nodo.f, nodo.id, nodo))

    def seleccionar_nodo(self):
        ''' Función que sacará y retornará el primer elemento de la frontera '''
        return heappop(self.frontera)
    
    def esta_vacia(self):
        ''' Función que indicará si la frontera está o no vacía '''
        return True if len(self.frontera) == 0 else False

    