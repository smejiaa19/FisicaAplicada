'''
Permitir introducir n cargas junto posiciones (pares ordenados)
Calcular vector fuerza neta < , > N y su magnitud
'''



def Input_info():
    Carga_objetivo = []
    magnitud = int(input('Ingesa la magnitud de la carga objetivo: \n'))
    posicion = int(input('Ingrese la posicion de la carga objetivo: \n'))
    Carga_objetivo.append(magnitud)
    Carga_objetivo.append(posicion)
    print(Carga_objetivo)    

Input_info()