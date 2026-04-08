'''
Permitir introducir n cargas junto posiciones (pares ordenados)
Calcular vector fuerza neta < , > N y su magnitud
'''

import math

class Carga:
    def __init__(self, magnitud, x, y):
        self.magnitud = magnitud
        self.x = x
        self.y = y

    def posicion(self):
        return (self.x, self.y)

    def obtener_distancia (self, carga):
        distancia_x = carga.x - self.x
        distancia_y = carga.y - self.y
        r = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return r
    
def input_cargas():
    n = int(input('Ingrese el numero de cargas: \n'))
    for i in range (n):
        print(f'Informacion Carga {n+1}\n')
        magnitud = float(input('Ingrese la magnitud de la carga: \n'))
        x = float(input('Ingrese la coordenada x de la carga: \n'))
        y = float(input('Ingrese la coordenada y de la carga: \n'))
