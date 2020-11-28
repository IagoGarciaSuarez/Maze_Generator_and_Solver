
#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
import os
import json
import numpy
import matplotlib.pyplot as plt
from Celda import Celda
from Direcciones import Direcciones

class Laberinto():
    def __init__(self, jsonFile, path, size = None):        
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
            self.savePath = path
            self.filas = size[0]
            self.columnas = size[1]
        self.laberinto = [[None for i in range(self.columnas)] for j in range(self.filas)]

        if not jsonFile:
            '''
            Cuando no hay json se genera un laberinto vacío que se va rellenando con celdas en las que
            se especificará si cada uno de sus cuatro vecinos son visitables además de su posición.
            La estructura de la clase Celda consiste en un valor, una tupla para indicar los vecinos y una tupla para
            la posición de la celda.
            '''
            for i in range(self.filas):
                for j in range(self.columnas):
                    self.laberinto[i][j] = Celda((False, False, False, False), (i, j), random.randint(0, 3))
            self.wilson()
            self.saveJson()
        else:
            '''
            Lee el json y le asigna las variables a cada celda para imprimirlo posteriormente.
            '''
            for cellPos in self.data_json["cells"]:
                cellPosTuple = eval(cellPos)
                row, col = cellPosTuple[0], cellPosTuple[1]
                self.laberinto[row][col] = Celda(numpy.array(self.data_json["cells"][cellPos]["neighbors"], dtype=bool), \
                    (row, col), numpy.array(self.data_json["cells"][cellPos]["value"], dtype=int))

        self.drawMaze()
    '''
    Algoritmo para generar el laberinto mediante el algoritmo de Wilson.
    '''
    def wilson(self):
        direcciones = Direcciones.direcciones
        valorDir = Direcciones.valorDir
        '''
        Se crea un array con todas las celdas no visitadas del laberinto, que al principio serán todas.
        '''
        celdasNoVisitadas = []
        numNoVisitadas = self.filas*self.columnas-1
        for x in range(self.filas):
            for y in range(self.columnas):
                celdasNoVisitadas.append(self.laberinto[x][y])
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
        celdaInicio y una celda visitada(en la primera iteración esa celda será celdaInicio) se generará un nuevo movimiento que
        resultará en la celda próxima a la actual. Ese movimiento lo guardaremos en caminoProvisional de manera que las
        coordenadas de la celda actual sean las coordenadas en la matriz caminoProvisional y la dirección el valor asignado
        a dicha posición.
        '''
        while numNoVisitadas > 0:
            '''
            Creamos una lista vacía para guardar posteriormente el camino final.
            '''
            caminoFinal = []
            caminoProvisional = [[None for i in range(self.columnas)] for j in range(self.filas)]
            celdaInicioCamino = random.choice(celdasNoVisitadas)
            inicioCaminoFila, inicioCaminoColumna = celdaInicioCamino.posicion[0], celdaInicioCamino.posicion[1]
            celdaActualFila, celdaActualColumna = inicioCaminoFila, inicioCaminoColumna
            caminoEncontrado = False

            while not caminoEncontrado:
                '''
                Elegimos una dirección aleatoria y obtenemos la celda destino a la que saltaríamos. Comprobamos que esté dentro
                de los límites y si es el caso, será válida.
                '''
                direccion = random.choice(direcciones)
                destinoFila, destinoColumna = celdaActualFila + valorDir[direccion][0], celdaActualColumna + valorDir[direccion][1]
                if destinoColumna in range(self.columnas) and destinoFila in range(self.filas):
                    caminoProvisional[celdaActualFila][celdaActualColumna] = direccion
                    '''
                    Si la celda destino ya está visitada, habremos unido el punto aleatorio con el camino ya excavado del laberinto.
                    Si no está visitada, la celda destino pasará a ser la celda actual.
                    '''
                    if self.laberinto[destinoFila][destinoColumna].visitada:
                        caminoEncontrado = True
                    else:
                        celdaActualFila, celdaActualColumna = destinoFila, destinoColumna
            '''
            Ahora que tenemos el camino provisional podemos seguirlo hasta llegar al final. Este camino resultante
            lo guardaremos en caminoFinal.
            '''
            fila, columna = inicioCaminoFila, inicioCaminoColumna
            while not self.laberinto[fila][columna].visitada:
                direccion = caminoProvisional[fila][columna]
                caminoFinal.append((fila, columna, direccion))
                fila, columna = fila + valorDir[direccion][0], columna + valorDir[direccion][1]
            '''
            Ya tenemos el camino final guardado en caminoFinal. Sólo falta poner en visitadas todas las celdas
            por las que pase este camino y cambiar el vecino de cada una a True según la dirección que tome.
            '''
            for c in caminoFinal:
                fila, columna, d = c[0], c[1], c[2]
                if d == "N":
                    self.laberinto[fila][columna].norte = True
                    self.laberinto[fila-1][columna].sur = True
                elif d == "E":
                    self.laberinto[fila][columna].este = True
                    self.laberinto[fila][columna+1].oeste = True 
                elif d == "S":
                    self.laberinto[fila][columna].sur = True
                    self.laberinto[fila+1][columna].norte = True
                elif d == "O":
                    self.laberinto[fila][columna].oeste = True
                    self.laberinto[fila][columna-1].este = True                
                self.laberinto[fila][columna].visitada = True
                numNoVisitadas -= 1
        return self.laberinto

    def saveJson(self):
        diccionarioJSON = dict()
        diccionarioJSON["rows"] = self.filas
        diccionarioJSON["cols"] = self.columnas
        diccionarioJSON["max_n"] = 4
        diccionarioJSON["mov"] = [[1,0],[0,1],[-1,0],[0,-1]]
        diccionarioJSON["id_mov"] = ["N","E","S","O"]

        cells = dict()
        for i in range(self.filas):
            for j in range(self.columnas):
                coordenadaXY = "(" + str(i) + ", " + str(j) + ")"
                diccionarioCoordenadaCelda = dict()
                diccionarioCoordenadaCelda["value"] = 0
                
                diccionarioCoordenadaCelda["neighbors"] = [self.laberinto[i][j].sur, self.laberinto[i][j].este, 
                self.laberinto[i][j].norte, self.laberinto[i][j].oeste]
                cells[coordenadaXY] = diccionarioCoordenadaCelda
                diccionarioJSON["cells"] = cells

        json.dump(diccionarioJSON, open(self.savePath, "w"), indent=3)

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
        plt.plot([0, self.columnas], [0, 0], color='black', linewidth=4)
        plt.plot([0, 0], [0, self.filas], color='black', linewidth=4)
        plt.plot([0, self.columnas], [self.filas, self.filas], color='black', linewidth=4)
        plt.plot([self.columnas, self.columnas], [self.filas, 0], color='black', linewidth=4)
        
        ax = plt.gca()

        for col in range(self.columnas):
            for row in range(self.filas):
                row_inv = self.filas - row - 1

    ############LINEAS################################################
                if not self.laberinto[row][col].sur:
                    plt.plot([col, col+1], [row_inv, row_inv], color = 'black',linewidth=3)
                if not self.laberinto[row][col].este:
                    plt.plot([col+1, col+1], [row_inv+1, row_inv], color = 'black',linewidth=3)
                if not self.laberinto[row][col].norte:
                    plt.plot([col, col+1], [row_inv+1, row_inv+1], color = 'black',linewidth=3)
                if not self.laberinto[row][col].oeste:
                    plt.plot([col, col], [row_inv, row_inv+1], color = 'black',linewidth=3)

    #########COLORES##################################################
                if self.laberinto[row][col].value == 0:
                    rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="white")
                    ax.add_patch(rectangle)
                if self.laberinto[row][col].value == 1:
                    rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="brown")
                    ax.add_patch(rectangle)
                if self.laberinto[row][col].value == 2:
                    rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="green")
                    ax.add_patch(rectangle)
                if self.laberinto[row][col].value == 3:
                    rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="blue")
                    ax.add_patch(rectangle)

        plt.axis("scaled")
        plt.savefig("Problemas_Generados/" + "puzzle_loop_" + str(self.filas) + "X" + str(self.columnas) + ".png")

    def getCelda (self, celda):
        return self.laberinto[celda[0]][celda[1]]