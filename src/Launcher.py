import sys
from Laberinto import Laberinto

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
            utilizarJson = int(input('1. Construir el laberinto a partir de un archivo .json.\n2. Generar el laberinto y guardarlo en un archivo .json\n'))
            if utilizarJson == 1:
                JSON = True
                print('Opción sin implementar')
                break
            if utilizarJson == 2:
                JSON = False
                SIZE = (int(input('Introduzca el número de columnas: ')), int(input('Introduzca el número de filas: ')))
                print(Laberinto(JSON, SIZE))
                break
            if utilizarJson not in [1, 2]: 
                print('Error al introducir la opción, por favor escriba una de las opciones válidas.')
        except ValueError:
            print('Error al introducir la opción, por favor escriba una de las opciones válidas.')
    
if __name__ == '__main__':
    menuStart()