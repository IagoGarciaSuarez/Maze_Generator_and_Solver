
#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
from Celda import Celda

#Check si se hace a partir de un .json (si se utiliza el argumento "-json")
JSON = False
if len(sys.argv) > 2:
    if sys.argv[1] == '-json':
        JSON = True
else:
    SIZE = (int(input('Ancho: ')), int(input('Largo: ')))

def generarLaberinto(filas, columnas):
    
    # generamos el laberinto sin ningún camino
    # celda = (norte, este, sur, oeste) - Sentido de las agujas del reloj
    # vecino = True
    # pared = False
    laberinto = [[None for i in range(columnas)] for j in range(filas)]
    celdasNoVisitadas = set()

    for i in range(filas):
        for j in range(columnas):
            # esquina superior izquierda
            if i == 0 and j == 0:
                laberinto[i][j] = Celda(False, True, True, False)
                celdasNoVisitadas.add(laberinto[i][j])            
            # esquina superior derecha
            elif i == 0 and j == filas - 1:
                laberinto[i][j] = Celda(False, False, True, True)
                celdasNoVisitadas.add(laberinto[i][j])
            # esquina inferior izquierda
            elif i == filas - 1 and j == 0:
                laberinto[i][j] = Celda(True, True, False, False)
                celdasNoVisitadas.add(laberinto[i][j])
            # esquina inferior derecha
            elif i == filas - 1 and j == columnas - 1:
                laberinto[i][j] = Celda(True, False, False, True)
                celdasNoVisitadas.add(laberinto[i][j])
            # fila superior
            elif i == 0:
                laberinto[i][j] = Celda(False, True, True, True)
                celdasNoVisitadas.add(laberinto[i][j])
            # fila inferior
            elif i == filas - 1 and 0 < j < columnas - 1:
                laberinto[i][j] = Celda(True, True, False, True)
                celdasNoVisitadas.add(laberinto[i][j])
            # columna izquierda
            elif j == 0:
                laberinto[i][j] = Celda(True, True, True, False)
                celdasNoVisitadas.add(laberinto[i][j])
             # columna derecha
            elif j == filas - 1:
                laberinto[i][j] = Celda(True, False, True, True)
                celdasNoVisitadas.add(laberinto[i][j])
            
            # celda interior
            else:
                laberinto[i][j] = Celda(True, True, True, True)
                celdasNoVisitadas.add(laberinto[i][j])
    celdasVisitadas = set()
    
    i = 0
    j = 0

#    while len(celdasNoVisitadas) > 0:
#        
#        celda = laberinto[i][j]
#        celdasVisitadas.add(celda)
#
#        i = random.randint(0, (filas - 1))
#        j = random.randint(0, columnas - 1)
#        
#        celdaActual = laberinto[i][j]
        
        #camino(celdaActual, celda)
   
    return laberinto

def dibujarLaberinto(laberinto):
    print(' ' + '_' * (SIZE[1] * 2))
    for col in range(SIZE[0]):
        for row in range(SIZE[1]):
            if row == 0:
                print('|', end = '')
            if not laberinto[col][row].sur and laberinto[col][row].este:
                print('__', end = '')
            if not laberinto[col][row].sur and not laberinto[col][row].este:
                print('__|', end = '')
            if laberinto[col][row].sur and not laberinto[col][row].este:
                print('  |', end = '')
            if laberinto[col][row].sur and laberinto[col][row].este:
                print('  ', end = '')
        print()
    
        
#print(" _", end="")
#print("|_|", end="")


lab = []

lab = generarLaberinto(SIZE[0], SIZE[1])

dibujarLaberinto(lab)