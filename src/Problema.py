from Laberinto import Laberinto
from Sucesores import Sucesores
from Estado import Estado

import json

class Problema():
    def __init__(self, JSON, path, size = None):
        self.pathProb = path + '.json'
        if JSON:
            self.problem_data = json.load(open(self.pathProb))
            self.laberinto = Laberinto(True, self.problem_data["MAZE"])
            self.start = eval(self.problem_data["INITIAL"])
            self.estado = Estado(self.laberinto[start[0]][start[1]])
            self.objective = eval(self.problem_data["OBJECTIVE"])
        else:
            self.pathMaze = path + '_maze.json'
            self.laberinto = Laberinto(False, self.pathMaze, size)
            self.start = (0, 0)
            self.objective = (size[0]-1, size[1]-1)
        
        self.sucesores = Sucesores()

    def objetivo(self, id):
        return id == self.objective

    def saveJSON(self):
        
        diccionarioJSON = dict()
        diccionarioJSON["INITIAL"] = self.start
        diccionarioJSON["OBJETIVE"] = self.objective
        diccionarioJSON["MAZE"] = self.pathMaze
        json.dump(diccionarioJSON, open(self.savePath, "w"), indent=3)  

