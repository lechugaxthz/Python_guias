from typing import List, Dict, Tuple
import math


# Ejercicio 1
# 1
def pertenece (sec : list[int], n: int) -> bool:  
    for i in range(0,len(sec)):
        if sec[i] == n :
            return True
    return False

# 2        
def divide_a_todos (sec: list[int], e: int) ->  bool:
    for i in sec:
        if i % e != 0 :
            return False
    return True

# 3
def suma_total (sec: list[int]) -> int:
    return sum(sec)

# 4 
def maximo (sec: list[int]) -> int:
    max(sec)
    
### aburrido xddd

## Ejercicio 2
# 1
def cerosEnPosicionesPares (sec: list[int]) -> list[int]:
    toReturn : list[int] = []
    for i in range(0, len(sec)):
        if i % 2 == 0:
            toReturn.append(0)
        else :
            toReturn.append(sec[i])
    return toReturn
print('ceros en posiciones pares')
print(cerosEnPosicionesPares([1,2,3,4,5]))


def pertenece_a_cada_uno (sec: list[list[int]], e: int) -> list[bool]:
    toReturn: list[bool] = []
    for lista in sec:
        toReturn.append(pertenece(lista, e))
    return toReturn

print 
        