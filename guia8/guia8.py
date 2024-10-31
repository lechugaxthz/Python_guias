from queue import LifoQueue as Lifo, Queue as Fifo

from random import *
import math

# Ejercicio 1
def generaar_nros_al_azar (cant : int, desde : int, hasta : int) -> Lifo[int] :
    p : Lifo[int] = Lifo()
    for x in range(cant):
        p.put(randint(desde, hasta))
    return p

def mostrar_pila (pila : Lifo[int]) -> None :
    listaVal: list[int] = []
    while not pila.empty():
        val : int = pila.get()
        listaVal.append(val)
        print(val)
    devolver_valores_a_pila(listaVal, pila)
        
def devolver_valores_a_pila (lista : list, pila : Lifo[int]) -> None :
    lista.reverse()
    for val in lista :
        pila.put(val)
        
        
#mostrar_pila(generaar_nros_al_azar(int(input('cuantos valores quieres ?')), int(input('desde que numero quieres partir ?')), int(input('hasta que numero quieres llegar ?'))))

# Ejercicio 2


# Ejercicio 3
def buscar_el_maximo (pila : Lifo[int]) -> int :
    if pila.empty():
        return 0

    maxVal : int = pila.get()
    listaVal: list[int] = [maxVal]

    while not pila.empty():
        val : int = pila.get()
        listaVal.append(val)
        if val >= maxVal:
            maxVal = val
    devolver_valores_a_pila(listaVal, pila)
    return maxVal

#print(buscar_el_maximo(generaar_nros_al_azar(int(input('cuantos valores quieres ?')), int(input('desde que numero quieres partir ?')), int(input('hasta que numero quieres llegar ?')))))

# Ejercicio 4
def busca_nota_maxima(pila : Lifo[tuple[str,int]]) -> tuple[str, int] :
    val1 : tuple[str, int] = pila.get()
    while not pila.empty() :
        val2 : tuple[str,int] = pila.get()
        if val2[1] > val1[1]:
            val1 = val2
    return val1


## bla bla bla

# Ejercicio 13

# 1
def armar_secuencia_de_bingo() -> Fifo[int] :
    cola : Fifo[int] = Fifo()
    rango : list[int] = []
    for i in range(100):
        rango.append(i)
    shuffle(rango)
    for i in rango:
        cola.put(i)
    return cola
    
def mostrar_cola (cola : Fifo[int]) -> None :
    listaVal: list[int] = []
    while not cola.empty():
        val : int = cola.get()
        listaVal.append(val)
        print(val)
    devolver_valores_a_cola(listaVal, cola)
        
def devolver_valores_a_cola (lista : list, cola : Fifo[int]) -> None :
    lista.reverse()
    for val in lista :
        cola.put(val)
        
#print(mostrar_cola(armar_secuencia_de_bingo()))

# 2
def jugar_carton_de_bingo(carton : list[int], bolillero : Fifo[int]) -> int :
    length_bolillero : list[int] = []
    list_length_carton : int = len(carton)
    cont :  int = 1
    while not bolillero.empty():
        if list_length_carton != 0:
            list_length_carton -= 1
        else:
            length_bolillero.append(cont)
        bolillero.get()
        cont += 1
    return math.prod(length_bolillero)

#print(jugar_carton_de_bingo([1,2,5,23,53,32,6], armar_secuencia_de_bingo()))


# Ejercicio 17
def calcular_promedio_por_estudiante(notas : list[tuple[str, int]]) -> dict[str,float]:
    notas_alumnos : dict[str, list[int]] = {}
    promedios : dict[str, float] = {}
    for nota in notas:
        if nota[0] in notas_alumnos:
            notas_alumnos[nota[0]].append(nota[1])
        else:
            notas_alumnos[nota[0]] = [nota[1]]
    for alumno in notas_alumnos.items():
        promedios[alumno[0]] = sum(alumno[1]) / len(alumno[1])
    return promedios

print (calcular_promedio_por_estudiante([('a',2),('b', 10),('a',5)]))