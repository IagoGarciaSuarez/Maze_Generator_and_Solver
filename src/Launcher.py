import sys
import os
from PIL import Image, ImageDraw
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

def saveToImage(dibujoLab):
    img = Image.new('RGB', (200, 100))
    d = ImageDraw.Draw(img)
    d.text((20, 20), dibujoLab, fill=(255, 0, 0))
    img.save('test.png')

def menuStart():
    print(asciiTitle)
    print('Bienvenid@, seleccione una opción para iniciar el programa:')
    while 1:
        try:
            utilizarJson = int(input('1. Construir el laberinto a partir de un archivo .json.\n2. Generar el laberinto y guardarlo en un archivo .json\n'))
            if utilizarJson == 1:
                JSON = True
                while True:
                    path = input("Introduzca el nombre del archivo json donde se almacena el laberinto:\n ")
                    if (os.path.exists(path)):
                        break
                    else:
                        print("La ruta del fichero que ha introducido no es válida.")
                dibujoLab = Laberinto(JSON, path)
                with open('test.txt', 'w') as f:
                    print(dibujoLab, file=f)
                saveToImage(str(dibujoLab))
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