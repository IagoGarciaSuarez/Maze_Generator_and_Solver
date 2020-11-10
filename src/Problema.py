from Laberinto import Laberinto
from Sucesores import Sucesores
from Estado import Estado

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
            self.laberinto = Laberinto(True, self.problem_data["MAZE"])
            self.start = eval(self.problem_data["INITIAL"])
            self.estado = Estado(self.laberinto.getCelda(self.start))
            self.objective = eval(self.problem_data["OBJETIVE"])
        else:
            self.pathMaze = path + '_maze.json'
            self.laberinto = Laberinto(False, self.pathMaze, size)
            self.start = (0, 0)
            self.objective = (size[0]-1, size[1]-1)
            self.saveJSON()
            
            self.sucesores = Sucesores()

            self.pathSuc = path + '.txt'
            self.saveSucTxt()

    def objetivo(self, id):
        return id == self.objective
    
    def saveJSON(self):
        diccionarioJSON = dict()
        diccionarioJSON["INITIAL"] = self.start
        diccionarioJSON["OBJECTIVE"] = self.objective
        diccionarioJSON["MAZE"] = self.pathMaze
        json.dump(diccionarioJSON, open(self.pathProb, "w"), indent=3)

    def saveSucTxt(self):

        suclistP = []
        costo = 1
        suclistP.append(("N",(1,0),costo))
        suclistP.append(("O",(2,0),costo))
        suclistP.append(("E",(3,0),costo))
        suclistP.append(("S",(4,0),costo))

        archivo = open(self.pathSuc, 'w')

        for i in suclistP:
            archivo.write(str(i) + '\n') 

        archivo.close()