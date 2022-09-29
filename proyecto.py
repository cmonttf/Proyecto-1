#*********************B*I*B*L*I*O*T*E*C*A*S********************

from ctypes import sizeof
from operator import index
from pickle import TRUE
import random as rd
from traceback import print_tb
from xmlrpc.client import boolean
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
            for j in range(n):
                if((abs(i-j)==abs(pob[k][i]-pob[k][j]))&(i!=j)): #cuenta choques en diagonal
                    cont=cont+1
                      
            if((n-1)==i):

                fit[k]=cont
                if(fit[k]==0):
                    print("AAAAA")
                cont=0

    

    return fit

#Seleccion de cruzamiento
def seleccion(v_fit,m_pob,prob_cruza):
    nuevo_fitness=np.zeros(np.size(v_fit))

    for i in range(np.size(v_fit)):
        if(v_fit[i]==0):
            v_fit[i]=1
        nuevo_fitness[i]=1/v_fit[i]/np.sum(v_fit)

    nuevo_proporcion=nuevo_fitness/(np.ones(np.size(nuevo_fitness))*np.sum(nuevo_fitness)) 
    nuevo_ruleta=np.zeros(np.size(nuevo_proporcion))                                    #nueva ruleta
    cont=0                      
                                

    for i in range(np.size(nuevo_proporcion)):
        if(i==0):
            nuevo_ruleta[i]=nuevo_proporcion[i]
        else:
            nuevo_ruleta[i]=nuevo_ruleta[(i-1)]+nuevo_proporcion[i]
        
        if(nuevo_ruleta[i]<(prob_cruza/100)):
            cont=cont+1
  
    return m_pob[0:cont]

#Cruzar dos individuos con un punto de cruza.
def cruza(pobl):
    dim=np.shape(pobl)
    p=dim[0]
    n=dim[1]

    m = np.zeros((p), dtype=int)
    m = np.arange(p)
    np.random.shuffle(m)   
    desendiente= np.zeros((p,n), dtype=int) 
    punto_cruza=0
    d=np.zeros(n, dtype=int) 
    print(m)
    for i in range(0,p-1,2):
        
        
        punto_cruza=np.random.randint(1,n)
        print("punto de cruza",punto_cruza)
        desendiente[m[i]]=np.concatenate([pobl[m[i]][0:punto_cruza],pobl[m[i+1]][punto_cruza:n]],axis=None)
        desendiente[m[i+1]]=np.concatenate([pobl[m[i+1]][0:punto_cruza],pobl[m[i]][punto_cruza:n]],axis=None)
        print(m)
    
    for i in range(p):
        if((desendiente[i]==d).all()):
            desendiente[i]=pobl[m[i]]

    print("\n",desendiente)

    

    return desendiente




#**************************************************************

#****************************M*A*I*N***************************

#Solicitamos los datos por pantalla

if len(sys.argv) == 5:
    semilla = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    prov_c = int(sys.argv[4])
    print("semilla            = ",semilla)
    print("tamaño de tablero   = ", n)
    print("tamaño de poblacion = ", p)
else:
    print("Error")
    print("Ingrese los parametros correctos: ''py proyecto.py semilla tamaño_tablero tamaño_poblacion probabilidad de cruza''")
#np.random.seed(semilla)


inicio = time.time()
np.random.seed(semilla)
    
encontrado = 0
mimatriz = ini_poblacion(n, p)
mifitness = fitness(mimatriz)
iteracion = 0
while (iteracion < 1000) and (encontrado == 0):
    for i in range(n):
        if mifitness[i] == 0:
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
        else:
            mimatriz = seleccion(mifitness,mimatriz,prov_c)
            cruza(mimatriz)
            mifitness = fitness(mimatriz)
            iteracion += 1


#print(mifitness)
#mimatriz = ini_poblacion(n, p)
#print(mimatriz,"\n")
#mifitness = fitness(mimatriz)
#print(mifitness)
#mimatriz =seleccion(mifitness,mimatriz,prov_c)
#print(mimatriz,"\n")

#cruza(mimatriz)


#**************************************************************
