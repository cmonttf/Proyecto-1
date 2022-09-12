# Proyecto 1 Algoritmos Metaheurísticos Inspirados en la Naturaleza: N-Reinas

1. Enunciado.

Se solicita desarrollar un programa utilizando el lenguaje de programación Python3 que implemente el problema de las N-Reinas usando algoritmos genéticos. 

Primero se debe definir como modelar el tablero en un cromosoma a través de una estructura de datos, como por ejemplo, un vector.

El código debe de tener al menos las siguientes funciones:
- Generar un número real randómico entre [0 y 1].
- Generar un número entero randómico entre [0 y N].
- Inicializar la población.
- Calcular el fitness de un individuo.
- Seleccionar dos individuos cno un punto de cruza.
- Mutar un individuo.
- Reducir la población. 

Además, se deben ingresar los siguientes parámetros:

- Valor de la semilla.
- Tamaño del tablero.
- Tamaño de la población.
- Probabilidad de cruza.
- Probabilidad de mutación.
- Número de iteraciones.

2. Programa

El código debe ser desarrollado usando una metodología de programación modular, es decir, debe haber uso de funciones y/o métodos que implementen de forma genérica los principales operadores genéticos los cuales serán usados en el programa principal.

El objetivo de esta implementación es poder crear una biblioteca de gunciones y/o métodos que puedan ser re-utilizados en cualquier otro programa que se pueda implementar en el futuro con el correspondiente ahorro en tiempo y líneas de código.