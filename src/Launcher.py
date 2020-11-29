import sys
import os
from Problema import Problema

asciiTitle = '''

███╗░░░███╗░█████╗░███████╗███████╗
████╗░████║██╔══██╗╚════██║██╔════╝
██╔████╔██║███████║░░███╔═╝█████╗░░
██║╚██╔╝██║██╔══██║██╔══╝░░██╔══╝░░
██║░╚═╝░██║██║░░██║███████╗███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
'''
def menuStart():
    print(asciiTitle)
    print('Bienvenid@, seleccione una opción para iniciar el programa:')
    p = problem()
    s = strat()
    p.busqueda_acotada(s)
    

def selectProblem():
    JSON = True
    while True:
        path = input("Introduzca el nombre del archivo json donde se almacena el problema (sin escribir la extensión .json):\n ")
        path = 'Ejemplos_resueltos/' + path + '.json'
        if (os.path.exists(path)):
            break
        else:
            print("La ruta del fichero que ha introducido no es válida. Recuerde escribirla sin la extensión .json.")
    p = Problema(JSON, path)
    return p

def createProblem():
    JSON = False
    SIZE = (int(input('Introduzca el número de filas: ')), int(input('Introduzca el número de columnas: ')))
    filas = SIZE[0]
    columnas = SIZE[1]
    path = 'Archivos_Generados/' + 'problema_' + str(filas) + 'x' + str(columnas)
    p = Problema(JSON, path, SIZE)
    return p

def problem():
    while 1:
        try:
            utilizarJson = int(input('1. Generar un problema a partir de un archivo .json.\n2. Crear el problema y guardarlo en un archivo .json\n'))
            if utilizarJson == 1:
                p = selectProblem()
                break

            if utilizarJson == 2:
                p = createProblem()
                break

            if utilizarJson not in [1, 2]: 
                print('Error al introducir la opción, por favor escriba una de las opciones válidas.')

        except ValueError:
            print('Error al introducir la opción, por favor escriba una de las opciones válidas.')
    return p
    
def strat():
    while 1:
        try:
            strat = int(input('1. Anchura\n2. Profunidad acotada\n3. Coste Uniforme\n4. Voraz\n5. A*\n'))
            if strat not in range(1, 6):
                print('Error al seleccionar la estrategia, por favor escriba una de las opciones válidas.')
            else:
                return strat

        except ValueError:
            print('Error al introducir la opción, por favor escriba una de las opciones válidas.')

if __name__ == '__main__':
    menuStart()