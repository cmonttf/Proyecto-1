#*********************B*I*B*L*I*O*T*E*C*A*S********************

from ctypes import sizeof
import random as rd
import numpy as np
import sys

#**************************************************************

#**********************F*U*N*C*I*O*N*E*S***********************

#Función randomica entre 0 y 1
def rand_bin():
    valor = rd.randint(0, 1)
    return valor

#Función randomico entre 0 y n
def rand_n(n):
    valor = rd.randint(0, n)
    return valor

#Funcion incializacion poblacion
def ini_poblacion(n, p):
    matriz = np.zeros((p,n), dtype=int)
    
    for i in range(p):
        matriz[i] = np.arange(0,n)
        np.random.shuffle(matriz[i])
    
    return matriz
     

#Función fitness que nos da el valor de que tan cercano a lo ideal estamos
def fitness(vector):
    tamanio = len(vector)
    return tamanio

#**************************************************************

#****************************M*A*I*N***************************

#Solicitamos los datos por pantalla
print("Ingrese los datos (tamaño gen, tamaño poblacion): ")
if len(sys.argv) == 4:
    semilla = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    print(semilla, n, p)
else:
    print("Error")
    print("Ingrese los parametros correctos: semilla, tamañotablero, tamañopoblacion")
    
np.random.seed(semilla)
    
mimatriz = ini_poblacion(n, p)

print(mimatriz)

#**************************************************************
