import matplotlib.pyplot as plt

def dibujar_laberinto(laberinto):

    plt.figure(figsize = (laberinto.columnas, laberinto.filas))
    plt.xticks([])
    plt.yticks()
    plt.plot([0, laberinto.columnas], [0, 0], color='black', linewidth=4)
    plt.plot([0, 0], [0, laberinto.filas], color='black', linewidth=4)
    plt.plot([0, laberinto.columnas], [laberinto.filas, laberinto.filas], color='black', linewidth=4)
    plt.plot([laberinto.columnas, laberinto.columnas], [laberinto.filas, 0], color='black', linewidth=4)
    
    ax = plt.gca()

    for col in range(laberinto.columnas):
        for row in range(laberinto.filas):
            row_inv = laberinto.filas - row - 1

############LINEAS################################################
            if not laberinto.laberinto[row][col].sur:
                plt.plot([col, col+1], [row_inv, row_inv], color = 'black',linewidth=3)
            if not laberinto.laberinto[row][col].este:
                plt.plot([col+1, col+1], [row_inv+1, row_inv], color = 'black',linewidth=3)
            if not laberinto.laberinto[row][col].norte:
                plt.plot([col, col+1], [row_inv+1, row_inv+1], color = 'black',linewidth=3)
            if not laberinto.laberinto[row][col].oeste:
                plt.plot([col, col], [row_inv, row_inv+1], color = 'black',linewidth=3)

#########COLORES##################################################
            if laberinto.laberinto[row][col].value == 0:
                rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="white")
                ax.add_patch(rectangle)
            if laberinto.laberinto[row][col].value == 1:
                rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="#8B4513")
                ax.add_patch(rectangle)
            if laberinto.laberinto[row][col].value == 2:
                rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="green")
                ax.add_patch(rectangle)
            if laberinto.laberinto[row][col].value == 3:
                rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="blue")
                ax.add_patch(rectangle)

    plt.axis("scaled")
    plt.savefig("Problemas_Generados/" + "puzzle_loop_" + str(laberinto.filas) + "x" + str(laberinto.columnas) + ".png")


def dibujar_solucion(laberinto,nodos,frontera,visitados,estrategia):
    '''
    Pensar en como pasar la estrategia y los vectores para frontera y solucion
    '''
    plt.figure(figsize = (laberinto.columnas, laberinto.filas))
    plt.xticks([])
    plt.yticks()
    plt.plot([0, laberinto.columnas], [0, 0], color='black', linewidth=4)
    plt.plot([0, 0], [0, laberinto.filas], color='black', linewidth=4)
    plt.plot([0, laberinto.columnas], [laberinto.filas, laberinto.filas], color='black', linewidth=4)
    plt.plot([laberinto.columnas, laberinto.columnas], [laberinto.filas, 0], color='black', linewidth=4)
    
    ax = plt.gca()

    for col in range(laberinto.columnas):
        for row in range(laberinto.filas):
            row_inv = laberinto.filas - row - 1

############LINEAS################################################
            if not laberinto.laberinto[row][col].sur:
                plt.plot([col, col+1], [row_inv, row_inv], color = 'black',linewidth=3)
            if not laberinto.laberinto[row][col].este:
                plt.plot([col+1, col+1], [row_inv+1, row_inv], color = 'black',linewidth=3)
            if not laberinto.laberinto[row][col].norte:
                plt.plot([col, col+1], [row_inv+1, row_inv+1], color = 'black',linewidth=3)
            if not laberinto.laberinto[row][col].oeste:
                plt.plot([col, col], [row_inv, row_inv+1], color = 'black',linewidth=3)

#########COLORES##################################################
            if  laberinto.laberinto[row][col].posicion in nodos:
                rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="red")
                ax.add_patch(rectangle)
            elif laberinto.laberinto[row][col].posicion in frontera:
                rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="blue")
                ax.add_patch(rectangle)
            elif laberinto.laberinto[row][col].posicion in visitados:
                rectangle = plt.Rectangle((col,row_inv),width=1,height=1,facecolor="green")
                ax.add_patch(rectangle)

    plt.axis("scaled")
    plt.savefig("Problemas_Generados/" + "solution_" + str(laberinto.filas) + "x" + str(laberinto.columnas) +"_"+str(estrategia)+"_20"+ ".png")
