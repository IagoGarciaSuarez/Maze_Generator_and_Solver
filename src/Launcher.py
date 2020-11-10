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
    while 1:
        try:
            utilizarJson = int(input('1. Generar un problema a partir de un archivo .json.\n2. Crear el problema y guardarlo en un archivo .json\n'))
            if utilizarJson == 1:
                JSON = True
                while True:
                    path = input("Introduzca el nombre del archivo json donde se almacena el problema (sin escribir la extensión .json):\n ")
                    path += '.json'
                    if (os.path.exists(path)):
                        break
                    else:
                        print(path)
                        print("La ruta del fichero que ha introducido no es válida. Recuerde escribirla sin la extensión .json.")
                Problema(JSON, path)
                break

            if utilizarJson == 2:
                JSON = False
                path = input("Introduzca el nombre del archivo json donde se almacenará el problema (sin escribir la extensión .json):\n ")
                SIZE = (int(input('Introduzca el número de filas: ')), int(input('Introduzca el número de columnas: ')))
                Problema(JSON, path, SIZE)
                break

            if utilizarJson not in [1, 2]: 
                print('Error al introducir la opción, por favor escriba una de las opciones válidas.')

        except ValueError:
            print('Error al introducir la opción, por favor escriba una de las opciones válidas.')
    
if __name__ == '__main__':
    menuStart()