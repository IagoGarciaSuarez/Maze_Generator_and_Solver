
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
    def wilson(self):
        direcciones = ["N", "E", "S", "O"]
        '''
        Se crea un array con todas las celdas no visitadas del laberinto, que al principio serán todas.
        '''
        celdasNoVisitadas = []
        for x in range(self.filas):
            for y in range(self.columnas):
                celdasNoVisitadas.append(self.laberinto[x][y])
        
        '''
        Se crean otros dos arrays: uno con las celdas que se hayan tocado en algún momento, aunque no se incluyan
        en el camino final, y otro con las celdas que seguirá el camino final. En ambos arrays se guardarán objetos 
        Movimiento que consistirán en una variable posición para establecer la posición de la celda actual y una 
        variable dirección que será una de las 4 direcciones (N, E, S, O) correspondientes a un vector dirección para 
        sumarle a la posición y obtener la siguiente celda.
        '''
        caminoProvisional = []
        caminoFinal = []
        '''
        Se establece la primera celda, que siempre estará sin visitar, se cambia a visitada y se quita de la lista de 
        celdas no visitadas.
        '''
        celdaInicio = random.choice(celdasNoVisitadas)
        celdaInicio.visitada = True
        celdasNoVisitadas.remove(celdaInicio)
        '''
        Ahora que tenemos la primera celda hecha, tenemos que encontrar otra celda aleatoria para poder unirlas y crear
        así el camino. Este proceso se repetirá en bucle hasta que no haya más celdas en celdasNoVisitadas.
        Empezamos escogiendo un item aleatorio de celdasNoVisitadas y otro de direcciones.
        Ahora podemos comenzar a buscar un camino. Mientras no se haya encontrado un camino de unión entre los puntos
        inicioCamino y una celda visitada(en la primera iteración esa celda será celdaInicio0) se generará un nuevo movimiento que
        resultará en la celda próxima a la actual.
        '''
        while celdasNoVisitadas:
            celdaActual = random.choice(celdasNoVisitadas)
            celdaActualX, celdaActualY = celdaActual.posicion[0], celdaActual.posicion[1]
            caminoTerminado = False

            while not caminoTerminado:
                direccion = random.choice(direcciones)
                if direccion == "N" and celdaActual.norte:
                    try:
                        'encontrar la posicion en camino provisional SOLO comparando las coordenadas'
                        posicionEnLista = caminoProvisional.index(Movimiento((celdaActualX, celdaActualY )))
                        'insertamos la misma celda actualizando la posicion'
                        caminoProvisional.insert(posicionEnLista,Movimiento(celdaActual.posicion, direccion))
                        caminoProvisional.pop(posicionEnLista+1)
                        
                        'hacemos que la celda actual sea la siguiente en la direccion elegida'
                        celdaActual.posicion[0], celdaActual.posicion[1]-1

                    except ValueError:

                        'si no esta la ponemos en la lista y actualizamos a la siguiente celda'
                        caminoProvisional.append(Movimiento(celdaActual.posicion, direccion))
                        celdaActual.posicion[0], celdaActual.posicion[1]-1
                    'Por ultimo miramos si la celda nueva es ya visitada si es asi salimos del bucle'
                    if celdaActual not in celdasNoVisitadas:
                        ultimaCelda = celdaActual
                        caminoTerminado = True
                 
                if direccion == "E" and celdaActual.Este:
                    for d in direcciones:
                        try:
                            posicionEnLista = caminoProvisional.index(Movimiento((celdaActualX + 1, celdaActualY + 0)))
                        
                        except ValueError:
                            caminoProvisional.append(Movimiento(celdaActual.posicion, direccion))            
                if direccion == "S" and celdaActual.Sur:
                    for d in direcciones:
                        try:
                            posicionEnLista = caminoProvisional.index(Movimiento((celdaActualX + 0, celdaActualY + 1)))

                        except ValueError:
                            caminoProvisional.append(Movimiento(celdaActual.posicion, direccion))  
                if direccion == "O" and celdaActual.Oeste:
                    for d in direcciones:
                        try:
                            posicionEnLista = caminoProvisional.index(Movimiento((celdaActualX - 1, celdaActualY + 0)))

                        
                        except ValueError:
                            caminoProvisional.append(Movimiento(celdaActual.posicion, direccion))            
                                      
            'ponemos en camino final la primera celda del provisional que sabremos que siempre sera parte del camino'                          
            caminoFinal.append(caminoProvisional[0])

            Final = False
            
            'aqui pasamos del camino provisional al final eligiendo celda validas'
            while not Final:
                cam
            


