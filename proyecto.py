#*********************B*I*B*L*I*O*T*E*C*A*S********************

from ctypes import sizeof
import random as rd
import numpy as np
import sys
import time

#**************************************************************

#**********************F*U*N*C*I*O*N*E*S***********************

#Función randomica entre 0 y 1
def rand_bin():
    valor = rd.randint(0, 1)
    return valor

#Función randomico entre 0 y n
def rand_n(n):
    valor = rd.randint(0,n)
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
    cont = 0
    fit = [] #vector fitness            
    for k in range(f):
        for i in range(c):
            for j in range(c):
                if(i!=j):
                    if(matriz[k][i]==matriz[k][j]): #cuenta los choques en horizontal
                        cont=cont+1
                    if(abs(i-j)==abs(matriz[k][i]-matriz[k][j])): #cuenta choques en diagonal
                        cont=cont+1
            if((c-1)==i):
                fit.append(cont)
                cont=0

    return fit

#seleccion de cruzamiento
def seleccion(v_fit,m_pob,prob_cruza):
    #print("suma fit= ",np.sum(v_fit))
    nuevo_fitness=np.ones(np.size(v_fit))/v_fit/(np.ones(np.size(v_fit))*np.sum(v_fit)) #nuevo fitness (1/fitness/sum(fitness))
    nuevo_proporcion=nuevo_fitness/(np.ones(np.size(v_fit))*np.sum(nuevo_fitness))      #nueva proporcion (nuevo fitness/sum(nuevo fitness))
    nuevo_ruleta=[]                                                                     #nueva ruleta

    for i in range(np.size(nuevo_proporcion)):
        if(i==0):
            nuevo_ruleta.append(nuevo_proporcion[i])
        else:
            nuevo_ruleta.append(nuevo_ruleta[(i-1)]+nuevo_proporcion[i])

    #print("nuevo fitnes = ",nuevo_fitness)
    #print("nuevo proporcion = ",nuevo_proporcion)
    #print("suma total de nuevo fitnes = ",np.sum(nuevo_fitness))
    #print("suma total de nuevo proporcion = ",np.sum(nuevo_proporcion))
    #print("nueva ruleta = ",nuevo_ruleta)
    a=0
    return a
#**************************************************************

#****************************M*A*I*N***************************

#Solicitamos los datos por pantalla

if len(sys.argv) == 5:
    semilla = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    prov_c = int(sys.argv[4])
    print("semilla             = ",semilla)
    print("tamaño de tablero   = ", n)
    print("tamaño de poblacion = ", p)
else:
    print("Error")
    print("Ingrese los parametros correctos: ''py proyecto.py semilla tamaño_tablero tamaño_poblacion probabilidad de cruza''")


inicio = time.time()
np.random.seed(semilla)
    
encontrado = 0
while encontrado == 0:
    mimatriz = ini_poblacion(n, p)
    mifitness = fitness(mimatriz)
    print(mimatriz)
    print(mifitness)


    for i in range(n):
        if int(mifitness[i]) == 0:
            print()
            print("****************************************")
            print("****************************************")
            print("Tablero encontrado:")
            print("Tablero: ", mimatriz[i])
            encontrado = 1
            fin = time.time()
            segundos = fin - inicio
            print("Tiempo transcurrido: ", segundos, " seg")
            print("****************************************")
            print("****************************************")
            print()

    #print(mimatriz)
    #print(mifitness)

    seleccion(mifitness,mimatriz,prov_c)

#**************************************************************
