from Laberinto import Laberinto
from Sucesores import Sucesores
from Estado import Estado
from Frontera import Frontera
from Nodo import Nodo

import json
import os

class Problema():
    def __init__(self, JSON, path, size = None):
        '''
        Hay un error en los problemas dados en donde indica la celda objetivo. Está escrito como "OBJETIVE" cuando debería
        estar escrito como "OBJECTIVE".
        '''
        self.pathProb = path + '.json'
        if JSON:
            self.problem_data = json.load(open(path))
            self.laberinto = Laberinto(True, self.problem_data["MAZE"])
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

        
    def saveTxt(self, nodo, estrategia):
        
        nodos = []
        while nodo.padre != None:
            nodos.append(nodo)
            nodo = nodo.padre
        
        nodos.reverse()
        filas = self.objective[0]
        columnas = self.objective[1]
        archivo = open("solution_" + str(filas) + "x" + str(columnas) + "_" + str(strategia) + ".txt",  'w')

        for n in nodos:
            archivo.write("[" + n.id + "][" + n.costo + "," + n.estado + "," + n.padre.estado.id + "," + n.accion + "," + n.p + "," + str(round(n.h,2)) + "," + str(round(n.f,2)) + "]")        
        
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
            n_actual = frontera.seleccionar_nodo()[2]
            print('select: ', n_actual.estado)

            if self.es_objetivo(n_actual.estado.id):
                self.print_solucion(n_actual)
                saveTxt(n_actual, estrategia)
                solucion = True
                
            elif n_actual.estado.id not in lista_visitados:
                lista_visitados.append(n_actual.estado.id)
                l_suc = self.sucesores.sucesores(n_actual, self.laberinto)
                l_nod = n_actual.crearListaNodosSuc(frontera, l_suc, n_actual, prof_max, estrategia)
                if l_nod != None:
                    for n in l_nod:
                        frontera.insertar_nodo(n)
                for f in frontera.frontera:
                    print('Frontera: {}, id: {}, cost: {}, h: {}, f: {}, dad: {}'.format(f[2].estado, f[2].id, f[2].costo, f[2].h, f[2].f, f[2].padre.estado))
                print('--------------')
        
        if solucion == False:
            print('No se ha encontrado ninguna solución.\n')