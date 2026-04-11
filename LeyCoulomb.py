import math
K = 9e9

class Carga:
    def __init__(self, magnitud, x, y):
        self.magnitud = magnitud
        self.x = x
        self.y = y

    def posicion(self):
        return (self.x, self.y)

    def obtener_distancia(self, carga):
        distancia_x = carga.x - self.x
        distancia_y = carga.y - self.y
        r = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return r
    
    def vector_hacia(self, carga):
        distancia_x = carga.x - self.x
        distancia_y = carga.y - self.y
        r = self.obtener_distancia(carga)

        if r == 0:
            return (0, 0)
        
        return (distancia_x / r, distancia_y / r)
    
    @staticmethod
    def calcular_fuerza(c1, c2):
        r = c1.obtener_distancia(c2)

        if r == 0:
            return (0, 0)
        
        F = K * (c1.magnitud * c2.magnitud) / (r**2)
        
        direccion_x, direccion_y = c1.vector_hacia(c2) 
        intensidad_x = F * direccion_x
        intensidad_y = F * direccion_y

        return (intensidad_x, intensidad_y)
    
    @staticmethod
    def fuerza_neta(cargas, objetivo):
        Fuerza_x_total = 0
        Fuerza_y_total = 0

        for carga in cargas:
            intensidad_x, intensidad_y = Carga.calcular_fuerza(objetivo, carga)
            Fuerza_x_total += intensidad_x
            Fuerza_y_total += intensidad_y

        return Fuerza_x_total, Fuerza_y_total
    
    @staticmethod
    def magnitud(intensidad_x, intensidad_y):
        return math.sqrt(intensidad_x**2 + intensidad_y**2)
    

def input_cargas():
    n = int(input('Ingrese el numero de cargas: \n'))
    cargas = []

    for i in range(n):
        print(f'Informacion Carga {i+1}\n')
        magnitud = float(input('Ingrese la magnitud de la carga: \n'))
        x = float(input('Ingrese la coordenada x de la carga: \n'))
        y = float(input('Ingrese la coordenada y de la carga: \n'))
        cargas.append(Carga(magnitud, x, y))

    return cargas

def main():
    print('Carga Objetivo')
    magnitud = float(input('Ingrese la magnitud de la carga objetivo: \n'))
    x = float(input('Ingrese la coordenada x: \n'))
    y = float(input('Ingrese la coordenada y: \n'))

    objetivo = Carga(magnitud, x, y)
    
    print('Cargas Externas')
    cargas = input_cargas()

    Fuerza_x_total, Fuerza_y_total = Carga.fuerza_neta(cargas, objetivo)
    magnitud_total = Carga.magnitud(Fuerza_x_total, Fuerza_y_total)

    print(f'Fuerza neta: {Fuerza_x_total} y {Fuerza_y_total} N')
    print(f'Magnitud de la fuerza: {magnitud_total} N')

if __name__== '__main__':
    main()