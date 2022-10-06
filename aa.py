import numpy as np


def ini_poblacion(n, p):
    matriz = np.zeros((p,n), dtype=int)
    
    for i in range(p):
        matriz[i] = np.arange(n)
        np.random.shuffle(matriz[i])
    
    print(matriz)
    return matriz

pob=ini_poblacion(4,10)
tamanio=np.shape(pob)
p=tamanio[0] #poblacion
n=tamanio[1]

fit=np.zeros(p,dtype=int)
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