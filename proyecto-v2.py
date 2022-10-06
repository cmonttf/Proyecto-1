#*********************B*I*B*L*I*O*T*E*C*A*S********************

import numpy as np
import sys
import time

#**************************************************************

#**********************F*U*N*C*I*O*N*E*S***********************

#Función randomica entre 0 y 1
def rand_bin():
    valor = np.random.randint(0, 1)
    return valor


#Función randomico entre 1 y n
def rand_n(n):
    valor = np.random.randint(0,n)
    return valor


#Funcion incializacion poblacion
def ini_poblacion(n, p):
    matriz = np.zeros((p,n), dtype=int)
    
    for i in range(p):
        matriz[i] = np.arange(n)
        np.random.shuffle(matriz[i])
    
    return matriz

#Funcion incializacion poblacion
def ini_poblacion(n, p):
    matriz = np.zeros((p,n), dtype=int)
    
    for i in range(p):
        matriz[i] = np.arange(n)
        np.random.shuffle(matriz[i])
    
    print(matriz)
    return matriz
     

#Función fitness que nos da el valor de que tan cercano a lo ideal estamos, calculo de coliciones
def fitness(pob):
    #max_choques=56
    tamanio=np.shape(pob)
    p=tamanio[0] #poblacion
    n=tamanio[1] #tamaño tablero
    fit=np.zeros(p,dtype=int) #vector final que nos dara el valor de colicion de cada tablero
    cont=0

    for k in range(p):
        for i in range(n):
            for j in range((i),n):
                if((abs(i-j)==abs(pob[k][i]-pob[k][j]))&(i!=j)): #cuenta choques en diagonal
                    cont=cont+1
                      
            if((n-1)==i):
                fit[k]=cont
                if(fit[k]==0):
                    print("AAAAA")
                cont=0
    print("fitness\n",fit)
    print("minimo = ",np.min(fit))
    return fit

#np.random.seed(2)
start = time.time()
fitness(ini_poblacion(18,500))
end = time.time()

print(end - start)