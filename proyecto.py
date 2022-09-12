#*********************B*I*B*L*I*O*T*E*C*A*S********************

from ctypes import sizeof
import random

#**************************************************************

#**********************F*U*N*C*I*O*N*E*S***********************

#Función randomica que nos da los valores alelos del gen
def rand_bin(n):
    vector = []
    for i in range(n):
        vector.append(random.randint(1, n))
    
    return vector

#Función fitness que nos da el valor de que tan cercano a lo ideal estamos
def fitness(vector):
    tamanio = len(vector)
    return tamanio

#**************************************************************

#****************************M*A*I*N***************************

#Solicitamos los datos por pantalla
print("Ingrese los datos: (tamaño gen, tamaño poblacion)")
n_gen = int(input())
n_pobl = int(input())


for i in range(n_pobl):
    vector = rand_bin(n_gen)
    print(rand_bin(n_gen))
    print(fitness(vector))

#**************************************************************