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

#Función randomico entre 1 y n
def rand_n(n):
    valor = rd.randint(0,(n-1))
    return valor

#Funcion incializacion poblacion
def ini_poblacion(n, p):
    matriz = np.zeros((p,n), dtype=int)
    
    for i in range(p):
        for j in range(n):
            matriz[i][j] = rand_n(n)
    
    return matriz
     

#Función fitness que nos da el valor de que tan cercano a lo ideal estamos, calculo de coliciones
def fitness(ini_poblacion):
    #max_choques=56
    tamanio=ini_poblacion.shape
    poblacion_inicial=ini_poblacion
    p=tamanio[0] #poblacion
    n=tamanio[1] #tamaño tablero
    fit=[]
    cont=0

    for k in range(p):
        for i in range(n):
            for j in range(n):
                if(i!=j):
                    if(poblacion_inicial[k][i]==poblacion_inicial[k][j]): #cuenta los choques en horizontal
                        cont=cont+1

                    if(abs(i-j)==abs(poblacion_inicial[k][i]-poblacion_inicial[k][j])): #cuenta choques en diagonal
                        cont=cont+1

            if((n-1)==i):
                fit.append(cont)
                cont=0

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
