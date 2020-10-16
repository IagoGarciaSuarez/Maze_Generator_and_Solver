import matplotlib.pyplot as plt

class Dibujo():
    def __init__(self):
        plt.figure(figsize = (10, 10))
        plt.xticks([])
        plt.yticks([])
        plt.plot([1, 1], [2, 1], color = 'black')
        plt.show()
        plt.style.use('dark_background')

laberinto = Dibujo()
