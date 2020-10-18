
#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
import json
import numpy
import matplotlib.pyplot as plt
from Celda import Celda
from Movimiento import Movimiento

class Laberinto():
    def __init__(self, jsonFile, path = None, size = None):        
        ''' 
        Si existe un json con los datos del laberinto, se cargarán; si no, 
        se asignarán los valores introducidos por el usuario.
        '''
        self.jsonFile = jsonFile
        if self.jsonFile:
            self.data_json = json.load(open(path))
            self.filas = self.data_json["rows"]
            self.columnas = self.data_json["cols"]
        else:
            self.filas = size[0]
            self.columnas = size[1]
        self.laberinto = [[None for i in range(self.columnas)] for j in range(self.filas)]
        self.celdasNoVisitadas = set()

        if not jsonFile:
            '''
            Cuando no hay json se genera un laberinto vacío que se va rellenando con celdas en las que
            se especificará si cada uno de sus cuatro vecinos son visitables además de su posición.
            La estructura de la clase Celda consiste en un valor, una tupla para indicar los vecinos y una tupla para
            la posición de la celda.
            '''
            for i in range(self.filas):
                for j in range(self.columnas):
                    # esquina superior izquierda
                    if i == 0 and j == 0:
                        self.laberinto[i][j] = Celda((False, True, True, False), (0, 0))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])            
                    # esquina superior derecha
                    elif i == 0 and j == self.columnas - 1:
                        self.laberinto[i][j] = Celda((False, False, True, True), (0, self.columnas-1))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])
                    # esquina inferior izquierda
                    elif i == self.filas - 1 and j == 0:
                        self.laberinto[i][j] = Celda((True, True, False, False), (self.filas-1, 0))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])
                    # esquina inferior derecha
                    elif i == self.filas - 1 and j == self.columnas - 1:
                        self.laberinto[i][j] = Celda((True, False, False, True), (self.filas-1, self.columnas-1))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])
                    # fila superior
                    elif i == 0:
                        self.laberinto[i][j] = Celda((False, True, True, True), (0, j))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])
                    # fila inferior
                    elif i == self.filas - 1:
                        self.laberinto[i][j] = Celda((True, True, False, True), (self.filas-1, j))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])
                    # columna izquierda
                    elif j == 0:
                        self.laberinto[i][j] = Celda((True, True, True, False), (i, 0))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])
                    # columna derecha
                    elif j == self.columnas - 1:
                        self.laberinto[i][j] = Celda((True, False, True, True), (i, self.columnas-1))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])
                    
                    # celda interior
                    else:
                        self.laberinto[i][j] = Celda((True, True, True, True), (i, j))
                        self.celdasNoVisitadas.add(self.laberinto[i][j])

            self.labGenerado = self.wilson()

        else:
            '''
            Lee el json y le asigna las variables a cada celda para imprimirlo posteriormente.
            '''
            for cellPos in self.data_json["cells"]:
                cellPosTuple = eval(cellPos)
                row, col = cellPosTuple[0], cellPosTuple[1]
                self.laberinto[row][col] = Celda(numpy.array(self.data_json["cells"][cellPos]["neighbors"], dtype=bool), (row, col))
    '''
    Las columnas corresponden al eje X y las filas al eje Y.
    Para acceder a las posiciones del laberinto se accederá de forma que laberinto[y][x]
    De esta forma, dibujaremos las paredes exteriores del laberinto y para cada celda el sur y el este desde arriba a abajo
    y de izquierda a derecha. 
    '''
    def drawMaze(self):
        plt.figure(figsize = (self.columnas, self.filas))
        plt.xticks([])
        plt.yticks()
        plt.plot([0, self.columnas], [0, 0], color='black', linewidth=2)
        plt.plot([0, 0], [0, self.filas], color='black', linewidth=2)
        plt.plot([0, self.columnas], [self.filas, self.filas], color='black', linewidth=2)
        plt.plot([self.columnas, self.columnas], [self.filas, 0], color='black', linewidth=2)

        for col in range(self.columnas):
            for row in range(self.filas):
                row_inv = self.filas - row - 1
                if not self.laberinto[row][col].sur:
                    plt.plot([col, col+1], [row_inv, row_inv], color = 'black')
                if not self.laberinto[row][col].este:
                    plt.plot([col+1, col+1], [row_inv, row_inv+1], color = 'black')
        plt.show()
    
    '''
    Algoritmo para generar el laberinto mediante el algoritmo de Wilson.
    '''
    # dada una celda, escoge una vecina aleatoria que no esté en el conjunto de las ya visitadas
    def escogerVecina(self, celdaActual):
        
        celdaVecina = None

        while celdaVecina == None:

            # esquina superior izquierda
            if celdaActual.posicion == (0,0) and celdaActual not in self.celdasVisitadas:
            
                vecina = random.randint(0,1)

                # celda derecha
                if vecina == 0:
                    celdaVecina = self.laberinto[0][1]
                
                # celda inferior
                else:
                    celdaVecina = self.laberinto[1][0]
        
            # esquina superior derecha
            elif celdaActual.posicion == (0, (self.columnas - 1)) and celdaActual not in self.celdasVisitadas:

                vecina = random.randint(0, 1)

                # celda izquierda
                if vecina == 0:
                    celdaVecina = self.laberinto[(self.filas - 2)][0]
                
                # celda inferior
                else:
                    celdaVecina = self.laberinto[1][(self.columnas - 1)]
        
            # esquina inferior izquierda
            elif celdaActual.posicion == ((self.filas - 1), 0) and celdaActual not in self.celdasVisitadas:

                vecina = random.randint(0, 1)

                # celda superior    
                if vecina == 0:
                    celdaVecina = self.laberinto[self.filas - 2][0]
                
                # celda derecha
                else:
                    celdaVecina = self.laberinto[self.filas - 1][1]
            
            # esquina inferior derecha
            elif celdaActual.posicion == ((self.filas - 1), (self.columnas - 1)) and celdaActual not in self.celdasVisitadas:

                vecina = random.randint(0, 1)

                # celda superior
                if vecina == 0:
                    celdaVecina = self.laberinto[self.filas - 2][self.columnas - 1]
                #celda izquierda
                else:
                    celdaVecina = self.laberinto[self.filas - 1][self.columnas - 2]
            
            # fila superior
            elif celdaActual.posicion[0] == 0 and celdaActual not in self.celdasVisitadas:

                vecina = random.randint(0, 2)

                # celda izquierda
                if vecina == 0:

                    celdaVecina = self.laberinto[0][celdaActual.posicion[1] - 1]
                
                # celda derecha
                elif vecina == 1:
                    
                    celdaVecina = self.laberinto[0][celdaActual.posicion[1] + 1]
                # celda de abajo
                elif vecina == 2:

                    celdaVecina = self.laberinto[1][celdaActual.posicion[1]]
                
            # fila inferior
            elif celdaActual.posicion[0] == self.filas - 1 and celdaActual not in self.celdasVisitadas:
                
                vecina = random.randint(0, 2)
                
                # celda izquierda
                if vecina == 0:

                    celdaVecina = self.laberinto[self.filas - 1][celdaActual.posicion[1] - 1]
                
                # celda derecha
                elif vecina == 1:
                    
                    celdaVecina = self.laberinto[self.filas - 1][celdaActual.posicion[1] + 1]
                
                # celda superior
                elif vecina == 2:

                    celdaVecina = self.laberinto[self.filas - 2][celdaActual.posicion[1]]


            # columna izquierda
            elif celdaActual.posicion[1] == 0 and celdaActual not in self.celdasVisitadas:
            
                vecina = random.randint(0, 2)
                # celda superior
                if vecina == 0:

                    celdaVecina = self.laberinto[celdaActual.posicion[0]- 1][0]
                
                # celda inferior
                elif vecina == 1:
                    
                    celdaVecina = self.laberinto[celdaActual.posicion[0] + 1][0]
                # celda derecha
                elif vecina == 2:

                    celdaVecina = self.laberinto[celdaActual.posicion[0]][1]
                
            # columna derecha
            elif celdaActual.posicion[1] == self.columnas - 1 and celdaActual not in self.celdasVisitadas:
                
                vecina = random.randint(0, 2)
                # celda superior
                if vecina == 0:

                    celdaVecina = self.laberinto[celdaActual.posicion[0] - 1][celdaActual.posicion[1]]
                
                # celda inferior
                elif vecina == 1:
                    
                    celdaVecina = self.laberinto[celdaActual.posicion[0] + 1][celdaActual.posicion[1]]
                # celda izquierda
                elif vecina == 2:

                    celdaVecina = self.laberinto[celdaActual.posicion[0]][celdaActual.posicion[1] - 1]

                
            # celda interior
            elif celdaActual not in self.celdasVisitadas:
                
                # 4 posibles vecinas
                vecina = random.randint(0, 3)
                # celda superior 
                if vecina == 0:

                    celdaVecina = self.laberinto[celdaActual.posicion[0] - 1][celdaActual.posicion[1]]
                
                #celda inferior
                elif vecina == 1:
                    
                    celdaVecina = self.laberinto[celdaActual.posicion[0] + 1][celdaActual.posicion[1]]

                # celda izquierda
                elif vecina == 2:

                    celdaVecina = self.laberinto[celdaActual.posicion[0]][celdaActual.posicion[1] - 1]
                
                # celda derecha
                else:

                    celdaVecina = self.laberinto[celdaActual.posicion[0]][celdaActual.posicion[1] + 1]

            return celdaVecina
            


    # genera un camino aleatorio sin bucles de celda inicial a una de las celdas visitadas
    def generarCamino(self, celdaInicial, conjuntoDeCeldasVisitadas):
        
        camino = list()
        
        conjuntoAuxiliar = set()

        for i in conjuntoDeCeldasVisitadas:
            
            conjuntoAuxiliar.add(i)

        celdaActual = celdaInicial
        
        celdaFinal = conjuntoAuxiliar.pop()
        
        posicionDePartida = celdaInicial.posicion

        while(celdaActual.posicion != celdaFinal.posicion):
            
            celda = self.escogerVecina(celdaActual)
            
            if celda not in camino:
                
                camino.append(celda)
                celdaActual = celda
            
           
           
            # hemos producido un bucle
            
            if celdaInicial.posicion == celdaActual.posicion:
                camino.clear()
                break
        
        return camino


    # celda = (norte, este, sur, oeste) - Sentido de las agujas del reloj
    # vecino = True
    # pared = False

    def excabarCamino(self, camino):

        i = 0
        
        while i < len(camino) - 1:
            
            celda = camino[i]
            
            celdaContigua = camino[i + 1]
            
            i = i + 1

            # indices de las posiciones de las celdas en el laberinto
            x1 = celda.posicion[0]
            y1 = celda.posicion[1]
            
            x2 = celdaContigua.posicion[0]
            y2 = celdaContigua.posicion[1]

            # esquina superior izquierda. Las contiguas pueden ser:
            if x1 == 0 and y1 == 0:
                
                # derecha
                if y1 == 1:
                    
                    self.laberinto[0][0].este = True
                    self.laberinto[0][1].oeste = True
                
                # inferior
                else:
                    
                    self.laberinto[0][0].sur = True
                    self.laberinto[1][0].norte = True
                           
            # esquina superior derecha. Las contiguas pueden ser:
            elif x1 == 0 and y1 == self.columnas - 1:

                #izquierda
                if y1 == y2 - 1:
                    
                    self.laberinto[0][self.columnas - 2].oeste = True
                    self.laberinto[0][1].oeste = True
                
                #inferior
                else:
                    
                    self.laberinto[x1][y1].sur = True
                    self.laberinto[x2][y2].norte = True
                    
            # esquina inferior izquierda. La contigua esta
            elif x1 == self.filas - 1 and y1 == 0:
                    
                    # arriba
                    if x2 == self.filas - 2 and y2 == 0:

                        self.laberinto[x1][y2].norte = True
                        self.laberinto[x2][y2].sur = True
                    
                    # a la derecha
                    else:
                        
                        self.laberinto[x1][y1].este = True
                        self.laberinto[x1][y2].oeste = True
                    

            # esquina inferior derecha. La contigua esta
            elif x1 == self.filas - 1 and y1 == self.columnas - 1:
                    
                # arriba
                if x1 == x2 - 1 and y1 == y2:

                    self.laberinto[x1][y1].norte = True
                    self.laberinto[x2][y2].sur = True
                    
                # a la izquierda
                else:

                    self.laberinto[x1][y1].oeste = True
                    self.laberinto[x2][y2].este = True

            # fila superior. La contigua esta
            elif x1 == 0:
                
                # a la izquierda
                if y1 == y2 - 1:
                    
                    self.laberinto[x1][y1].oeste = True
                    self.laberinto[x2][y2].este = True
                
                # a la derecha
                elif y1 == y2 + 1:

                    self.laberinto[x1][y1].este = True
                    self.laberinto[x2][y2].oeste = True

                # debajo
                else:

                    self.laberinto[x1][y1].sur = True
                    self.laberinto[x2][y2].norte = True
                

            # fila inferior. La contigua esta a la
            elif x1 == self.filas - 1:

                # izquierda
                if y1 == y2 - 1:
                    
                    self.laberinto[x1][y1].oeste = True
                    self.laberinto[x2][y2].este = True
                
                #derecha
                elif y1 == y2 + 1:

                    self.laberinto[x1][y1].este = True
                    self.laberinto[x2][y2].oeste = True

                # arriba
                else:

                    self.laberinto[x1][y1].norte = True
                    self.laberinto[x2][y2].sur = True
                    
            # columna izquierda. La contigua esta
            elif y1 == 0:

                # arriba
                if x1 == x2 - 1:
            
                    self.laberinto[x1][y1].norte = True
                    self.laberinto[x2][y2].sur = True
                    
                # abajo
                elif x1 == x2 + 1:

                    self.laberinto[x1][y1].sur = True
                    self.laberinto[x2][y2].norte = True

                # a la derecha
                else:

                    self.laberinto[x1][y1].este = True
                    self.laberinto[x2][y2].oeste = True

            # columna derecha. La contigua esta
            elif x1 == self.columnas - 1:

                # arriba
                if x1 == x2 - 1:

                    self.laberinto[x1][y1].sur = True
                    self.laberinto[x2][y2].norte = True                    
                    
                # abajo
                if x1 == x2 + 1:
                    
                    self.laberinto[x1][y1].norte = True
                    self.laberinto[x2][y2].sur = True
                
                # a la izquierda
                else:

                    self.laberinto[x1][y1].oeste = True
                    self.laberinto[x2][y2].este = True
                                    
            # celda interior. La contigua esta
            else:

                # arriba
                if x1 == x2 - 1 and y1 == y2:
                    
                    self.laberinto[x1][y1].sur = True
                    self.laberinto[x2][y2].norte = True

                # abajo
                elif x1 == x2 + 1 and y1 == y2:

                    self.laberinto[x1][y1].norte = True
                    self.laberinto[x2][y2].sur = True

                # izquierda
                elif x1 == x2 and y1 == y2 + 1:

                    self.laberinto[x1][y1].este = True
                    self.laberinto[x2][y2].oeste = True 

                # derecha
                else:

                    self.laberinto[x1][y1].oeste = True
                    self.laberinto[x2][y2].este = True

                                       
    def wilson(self):
        
        # partimos de la celda inicial y la contamos como visitada
        i = 0
        j = 0
        
        celdaInicial = self.laberinto[i][j]
        self.celdasVisitadas.add(celdaInicial)
        
        #elegimos otra celda distinta de manera aleatoria y la añadimos a las visitadas
        
        while not (i == 0 and j == 0):
            i = random.randint(0, (self.filas - 1))
            j = random.randint(0, (self.columnas - 1))

        celdaActual = self.laberinto[i][j]
        self.celdasVisitadas.add(celdaActual)

        while len(self.celdasNoVisitadas) > 0:
            
            camino = self.generarCamino(celdaActual, self.celdasVisitadas)

            for i in camino:
                self.celdasVisitadas.add(i)
            
            self.excabarCamino(camino)

            celdaActual = self.celdasNoVisitadas.pop()