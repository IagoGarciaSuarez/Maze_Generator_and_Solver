from Laberinto import Laberinto
from Sucesores import Sucesores
from Estado import Estado
from Frontera import Frontera
from Nodo import Nodo

import json

class Problema():
    def __init__(self, JSON, path, size = None):
        '''
        Hay un error en los problemas dados en donde indica la celda objetivo. Está escrito como "OBJETIVE" cuando debería
        estar escrito como "OBJECTIVE".
        '''
        self.pathProb = path + '.json'
        if JSON:
            self.problem_data = json.load(open(path))
            self.laberinto = Laberinto(True, 'Ejemplos_resueltos/' + self.problem_data["MAZE"])
            self.start = eval(self.problem_data["INITIAL"])
            self.objective = eval(self.problem_data["OBJETIVE"])
        else:
            self.pathMaze = path + '_maze.json'
            self.pathSuc = path + '.txt'
            self.laberinto = Laberinto(False, self.pathMaze, size)
            self.start = (0, 0)
            self.objective = (size[0]-1, size[1]-1)
            self.saveJSON()
        
        self.estado = Estado(self.laberinto.getCelda(self.start))
        self.sucesores = Sucesores()

    def es_objetivo(self, id):
        return id == self.objective 
    
    def saveJSON(self):
        diccionarioJSON = dict()
        diccionarioJSON["INITIAL"] = self.start
        diccionarioJSON["OBJECTIVE"] = self.objective
        diccionarioJSON["MAZE"] = self.pathMaze
        json.dump(diccionarioJSON, open(self.pathProb, "w"), indent=3)
    
    def saveTxt(self, nodo, estrat):
        nodos = []        

        while nodo.padre != None:
            nodos.append(nodo)
            nodo = nodo.padre
        
        nodos.reverse()

        filas = self.objective[0] + 1
        columnas = self.objective[1] + 1

        if(estrat == 1):
            estrategia = 'BREADTH'
        
        elif(estrat == 2):
            estrategia = 'DEPTH'

        elif(estrat == 3):
            estrategia = 'UNIFORM'

        elif(estrat == 4):
            estrategia = 'GREEDY'

        else:
            estrategia = 'A'
        
        archivo = open("Problemas_Generados/solution_" + str(filas) + "X" + str(columnas) + "_" + estrategia + ".txt", 'w')
        
        for n in nodos:
            archivo.write("[" + str(n.id) + "]" + "[" + str(n.costo) + ", " + str(n.estado) + ", " + 
            str(n.padre.estado.id) + ", " + str(n.accion) + ", " + str(n.p) + ", " + str(round(n.h,2)) + ", " + str(round(n.f,2)) + "]\n")
        
        archivo.close()
    
    def print_solucion(self, n): 
        ''' 
        Función encargado de imprimir la lista de nodos que llevan a la solución. El formato será:
        [id][costo, estado, id_padre, accion, profundidad, h, value]
        '''
        nodos = []
        while n.padre != None:
            nodos.append(n)
            n = n.padre
        print("[{}][{}, {}, {}, {}, {}, {}, {}]".format(n.id, n.costo, n.estado, n.padre, n.accion, n.p, round(n.h,2), round(n.f,2)))
        nodos.reverse()
        for n in nodos:
            print("[{}][{}, {}, {}, {}, {}, {}, {}]".format(n.id, n.costo, n.estado, n.padre.estado.id, n.accion, n.p, round(n.h,2), round(n.f,2)))

    def calcularHeuristica(self):
        h = abs(self.estado.celda.posicion[0] - self.objective[0]) + abs(self.estado.celda.posicion[1] + self.objective[1])
        return h

    def busqueda_acotada(self, estrategia, prof_max=5):
        '''
        Función encargada de encontrar la solución dada una estrategia.
        '''
        frontera = Frontera()
        lista_visitados = []
        solucion = False
        test = None
        '''
        Creamos el nodo inicial, cuyo estado va a ser la celda inicial del laberinto.
        '''
        n_inicial = Nodo(frontera.next_id, 0, self.estado, None, 'None', 0, 0, self.objective)
        n_inicial.f = n_inicial.calcularValor(estrategia, n_inicial)
        frontera.insertar_nodo(n_inicial)
        frontera.next_id += 1

        while not solucion and not frontera.esta_vacia():
            n_actual = frontera.seleccionar_nodo()[4]

            if self.es_objetivo(n_actual.estado.id):
                self.print_solucion(n_actual)
                self.saveTxt(n_actual, estrategia)
                solucion = True
                
            elif n_actual.estado.id not in lista_visitados:
                lista_visitados.append(n_actual.estado.id)
                l_suc = self.sucesores.sucesores(n_actual, self.laberinto)
                l_nod = n_actual.crearListaNodosSuc(frontera, l_suc, n_actual, prof_max, estrategia)
                if l_nod != None:
                    for n in l_nod:
                        frontera.insertar_nodo(n)
        
        if solucion == False:
            print('No se ha encontrado ninguna solución.\n')