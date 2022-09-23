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
     

#Función fitness que nos da el valor de que tan cercano a lo ideal estamos, calculo de coliciones
def fitness(matriz):
    tamanio = matriz.shape #se obtene tamaño de la matriz en un vector
    f = int(tamanio[0]) #tamaño de las filas o poblacion
    c = int(tamanio[1]) #tamaño de las columnas o tablero
    

    for i in range(f):
        fit = [] #vector fitness
        vector = []
        vector = matriz[i]
        cont = 0
        for j in range(c):
            
            #if(vector[j] )
            aux = int(vector[j])
            k = j + 1
            
            for k in range(c):
                der = aux + k
                izq = aux - k
                if vector[k] == der:
                    cont = cont + 1
                else:
                    if vector[k] == izq:
                        cont = cont + 1
        fit.append(cont)

    return fit


#**************************************************************

#****************************M*A*I*N***************************

#Solicitamos los datos por pantalla
if len(sys.argv) == 4:
    semilla = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    print(semilla, n, p)
else:
    print("Error")
    print("Ingrese los parametros correctos: ''py proyecto.py semilla tamaño tablero tamaño poblacion''")
    
np.random.seed(semilla)
    
mimatriz = ini_poblacion(n, p)
mifitness = fitness(mimatriz)

print(mimatriz)
print(mifitness)

#**************************************************************
