from Laberinto import Laberinto
from Sucesores import Sucesores
from Estado import Estado

import json
import random
import os

class Problema():
    def __init__(self, JSON, path, size = None):
        '''
        Hay un error en los problemas dados en donde indica la celda objetivo. Está escrito como "OBJETIVE" cuando debería
        estar escrito como "OBJECTIVE".
        '''
        if JSON:
            self.problem_data = json.load(open(path))
            self.laberinto = Laberinto(True, self.problem_data["MAZE"])
            self.start = eval(self.problem_data["INITIAL"])
            self.estado = Estado(self.laberinto.getCelda(self.start))
            self.objective = eval(self.problem_data["OBJETIVE"])
        else:
            self.pathMaze = path + '_maze.json'
            self.laberinto = Laberinto(False, self.pathMaze, size)
            self.start = (0, 0)
            self.objective = (size[0]-1, size[1]-1)
        
        #self.sucesores = Sucesores()

        #IDNodo = 0
        
        self.pathSuc = path + '.txt'

        archivo = open(self.pathSuc, 'w')

        for i in range(10):
        
            fila = random.randint(0, self.laberinto.filas - 1)
            columna = random.randint(0, self.laberinto.columnas - 1)
            nodo = Estado(self.laberinto.getCelda((fila, columna)))

            #nodoFrontera = Nodo(IDNodo, 0, nodo, 0 , 0, 0, 0)
            #IDNodo = IDNodo + 1
            #frontera = Frontera()
            #frontera.insertar_nodo(nodoFrontera)
            
            suc = Sucesores()
            listaSucesores = suc.sucesores(nodo, self.laberinto)
            archivo.write('SUC((' + str(fila) + ',' + str(columna) + '))=')
            archivo.write(str(listaSucesores))
            archivo.write('\n')
                
        archivo.close()

    def objetivo(self, id):
        return id == self.objective
    
    def saveJSON(self):
        diccionarioJSON = dict()
        diccionarioJSON["INITIAL"] = self.start
        diccionarioJSON["OBJECTIVE"] = self.objective
        diccionarioJSON["MAZE"] = self.pathMaze
        json.dump(diccionarioJSON, open(self.pathProb, "w"), indent=3)