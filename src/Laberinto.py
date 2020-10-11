
#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
from Celda import Celda

class Laberinto():
    def __init__(self, json, size = None):        
        ''' 
        generamos el laberinto sin ningún camino
        celda = (norte, este, sur, oeste) - Sentido de las agujas del reloj
        vecino = True
        pared = False
        '''
        self.json = json
        self.filas = size[0]
        self.columnas = size[1]
        self.laberinto = [[None for i in range(self.columnas)] for j in range(self.filas)]
        self.celdasNoVisitadas = set()

        for i in range(self.filas):
            for j in range(self.columnas):
                # esquina superior izquierda
                if i == 0 and j == 0:
                    self.laberinto[i][j] = Celda(False, True, True, False)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])            
                # esquina superior derecha
                elif i == 0 and j == self.filas - 1:
                    self.laberinto[i][j] = Celda(False, False, True, True)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])
                # esquina inferior izquierda
                elif i == self.filas - 1 and j == 0:
                    self.laberinto[i][j] = Celda(True, True, False, False)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])
                # esquina inferior derecha
                elif i == self.filas - 1 and j == self.columnas - 1:
                    self.laberinto[i][j] = Celda(True, False, False, True)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])
                # fila superior
                elif i == 0:
                    self.laberinto[i][j] = Celda(False, True, True, True)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])
                # fila inferior
                elif i == self.filas - 1:
                    self.laberinto[i][j] = Celda(True, True, False, True)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])
                # columna izquierda
                elif j == 0:
                    self.laberinto[i][j] = Celda(True, True, True, False)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])
                # columna derecha
                elif j == self.filas - 1:
                    self.laberinto[i][j] = Celda(True, False, True, True)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])
                
                # celda interior
                else:
                    self.laberinto[i][j] = Celda(True, True, True, True)
                    self.celdasNoVisitadas.add(self.laberinto[i][j])

        '''
        Para dibujar el laberinto se irá imprimiendo línea por línea cada celda, únicamente comprobando si 
        las celdas del sur y del este son visitables. En caso de que no lo sean, según la combinación de ambas
        no visitables, se escribirán las paredes. Ädemás para la pared norte y oeste se escribirán los caracteres
        manualmente ya que sólo se escribirán las paredes del sur y del este, por lo que no habría celdas
        que comprobasen ese lado.
        '''
    def __str__(self):
        dibujo = ' ' + '_' * (self.columnas * 2) + '\n'
        for col in range(self.filas):
            for row in range(self.columnas):
                if row == 0:
                    dibujo += ('|')
                if not self.laberinto[col][row].sur and self.laberinto[col][row].este:
                    dibujo += ('__')
                if not self.laberinto[col][row].sur and not self.laberinto[col][row].este:
                    dibujo += ('__|')
                if self.laberinto[col][row].sur and not self.laberinto[col][row].este:
                    dibujo += ('  |')
                if self.laberinto[col][row].sur and self.laberinto[col][row].este:
                    dibujo += ('  ')
            dibujo += ('\n')
        return dibujo