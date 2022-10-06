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
    print("fitness\n",fit)
    return fit


#Seleccion de cruzamiento
def seleccion(v_fit,m_pob,prob_cruza):
    if(np.amin(v_fit)==0):
        i=int(np.where(v_fit==0)[0][0])
        return i

    else:
        nuevo_fitness=np.zeros(np.size(v_fit))
        tamanio=np.shape(m_pob)
        p=tamanio[0] #poblacion

        nuevo_fitness=np.ones(np.size(v_fit))/v_fit/(np.ones(np.size(v_fit))*np.sum(v_fit)) 
        nuevo_proporcion=nuevo_fitness/(np.ones(np.size(nuevo_fitness))*np.sum(nuevo_fitness)) 
        nuevo_ruleta=np.zeros(np.size(nuevo_proporcion))                                    
        cont=0                      
        
        for i in range(np.size(nuevo_proporcion)):
            if(i==0):
                nuevo_ruleta[i]=nuevo_proporcion[i]
            else:
                nuevo_ruleta[i]=nuevo_ruleta[(i-1)]+nuevo_proporcion[i]
            
            if(nuevo_ruleta[i]<=(prob_cruza/100)):
                cont=cont+1

        cont_p=0
        for i in range(cont+1,p):
            m_pob[i]=m_pob[cont_p]
            cont_p=cont_p+1
        
        return m_pob

#Cruzar dos individuos con un punto de cruza.
def cruza(pobl):
    dim=np.shape(pobl)
    p=dim[0]
    n=dim[1]

    pob_aux=np.zeros((p), dtype=int)
    pob_aux = np.arange(p)
    np.random.shuffle(pob_aux)
    descendiente= np.zeros((p,n), dtype=int) 
    punto_cruza=0
    cont=0
   

    while(cont<p):

            if(np.array_equal(pobl[cont],pobl[(cont+1)])==False):
                punto_cruza=np.random.randint(1,n)
                descendiente[cont]=np.append(pobl[cont][0:punto_cruza],pobl[(cont+1)][punto_cruza:n])
                descendiente[(cont+1)]=np.append(pobl[(cont+1)][0:punto_cruza],pobl[cont][punto_cruza:n])
                cont=cont+2
    
         

    return descendiente

#Coreeccion de individuos cruzados
def correccion(cruza):
    dim=np.shape(cruza)
    p=dim[0]
    n=dim[1]
    aux=np.zeros((p,n), dtype=int)
    
    for i in range(p):
            for k in range(n):
                aux[i][cruza[i][k]]=1 

    for i in range(p):
        for j in range(n):
            for k in range(j):
                for l in range(n):
                    if(cruza[i][j]==cruza[i][k] and j!=k):
                        if(aux[i][l]==0):
                            cruza[i][j]=l

    return cruza     
                
#mutacion
def mutacion(pob,prob_muta):
    dim=np.shape(pob)
    p=dim[0]
    n=dim[1]
    prob=np.ones(p,dtype=float)
    matrizaux = np.zeros((p,n), dtype=int)
    cont=0
    cont_r=0
    m=0

    for i in range(p):
        prob[i]=np.random.rand()
        if(prob[i]<=prob_muta/100):
            matrizaux[cont]=pob[i]
            cont=cont+1

    for j in range(cont,p):
        matrizaux[j]=matrizaux[cont_r]
        cont_r=cont_r+1

    for kk in range(p):
        r_aux1=np.random.randint(0,n)
        r_aux2=np.random.randint(0,n)
        while(m==0):
            if(r_aux2==r_aux1):
                r_aux2=np.random.randint(0,n)
            else:
                m=1
        aux1=matrizaux[kk][r_aux1]
        aux2=matrizaux[kk][r_aux2]
        matrizaux[kk][r_aux2]=aux1
        matrizaux[kk][r_aux1]=aux2

    return matrizaux







#**************************************************************

#****************************M*A*I*N***************************

#Solicitamos los datos por pantalla

if len(sys.argv) == 7:
    semilla = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    probabilidad_cruza = int(sys.argv[4])
    probabilidad_mutacion=int(sys.argv[5])
    iteraciones=int(sys.argv[6])
    print("semilla            = ",semilla)
    print("tamaño de tablero   = ", n)
    print("tamaño de poblacion = ", p)
else:
    print("Error")
    print("Ingrese los parametros correctos: ''py proyecto.py semilla tamaño_tablero tamaño_poblacion probabilidad de cruza''")
#np.random.seed(semilla)




contador=0
posicion_final=0
mimatriz = ini_poblacion(n, p)
while(contador<iteraciones):
    print(mimatriz)
    mifitness = fitness(mimatriz)
    if(type(seleccion(mifitness,mimatriz,probabilidad_cruza))==np.ndarray):
        correccion(cruza(mimatriz))
        mimatriz=mutacion(mimatriz,probabilidad_mutacion)

    elif(type(seleccion(mifitness,mimatriz,probabilidad_cruza))==int):
        posicion_final=seleccion(mifitness,mimatriz,probabilidad_cruza)
        break
    contador=contador+1

print("mejor posicion = ",mimatriz[posicion_final])
#**************************************************************
