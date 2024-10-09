import math
import time

# ejercicio 1
## a
def imprimir_hola_mundo () :
    print ("hola mundo")
## b
def raizDe2 () -> float :
    return (round(math.sqrt(2)), 4)
    
## c
def factorial (n:int) -> int :
    return math.factorial(n)

## d
def perimetro () -> float:
    return math.pi * 2

# ejerciocio 2
## a
def imprimir_saludo (nombre : str) :
    print ("Hola " + nombre)

## b
def raiz_cuadrada_de (n :int) -> float :
    return math.sqrt(n)

## c
def fahreheit_a_calsius (temp_far : float) -> float :
    return ((temp_far-32)* 5)/9

## e
def es_multiplo_de (n:int,m:int) -> bool :
    return m % n == 0

## f
def es_par (n:int) -> bool :
    return es_multiplo_de (2,n)

## g
def cantidad_de_pizzas (personas:int, min_cant_prociones:int) -> int :
    return math.ceil((personas * min_cant_prociones) / 8)

# ejercicio 3
## a
def alguno_es_0 (n:int, m:int) -> bool :
    return n == 0 or m == 0

## b
def ambos_son_0 (n:int, m:int) -> bool :
    return n == 0 and m == 0

## c
def es_nombre_largo (nombre: str) -> bool :
    return len(nombre) >= 3 and len(nombre) <= 8

# ejercicio 4
#### hacer despues !!!!

# ejercicio 5
## a
def devolver_el_doble_si_es_par (n:int) -> int :
    res: int = n
    if es_multiplo_de (2,n) : 
        res = 2 * n
    return res

## b
def devolver_valor_si_es_par_sino_el_que_sigue (n: int) -> int :
    res: int = n
    if es_multiplo_de (2,n) : 
        res = 2 * n
    else : 
        res = n+1
    return res

## c
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (n: int) -> int :
    if es_multiplo_de (3,n) and not es_multiplo_de (9,n) :
        n = n*2
    else :
        if es_multiplo_de (9,n) :
            n = n*3
    return n

# ejercicio 6
## a
def printNNumeros (n:int) :
    condicion : bool = True
    contador : int = 1
    while condicion :
        print (contador)
        contador +=1
        if contador == n+1 :
            condicion = False
    return

## b
def printNNumParesIn (n:int, m:int) :
    condicion : bool = True
    contador : int = n
    if not es_par (n) :
        contador += 1
    while condicion :
        print (contador)
        contador += 2
        if contador >= m+1 :
            condicion = False
    return

## d
def cuentaRegresiva (n:int) :
    if n<0 :
        n *= (-1)
    
    while n>0 :
        print(n)
        time.sleep(1)
        n-=1
        
    print ("despegue!")
    
# ejercicio 7
## a
def forPrintNNumeros (n:int) :
    for i in range(1,n) :
        print (i)
        
## b
def forPrintNNumParesIn (n:int, m:int) :
    for i in range(n,m) :
        print (i)
        
## d
def forCuentaRegresiva (n:int) :
    for i in range (n,0,-1) :
        print (i)
        time.sleep(1)
    print ("despliegue!")
    
    
# ejercicio 9
## a
### devuelve 4 porque sobre escribe g 3 veces y vale 0 inicial y a ro se le pasa 1 como parametro por tanto x + g == 1 + 3

## b
### devuelve 2 porque por mas que aparezca que sobre escriban g, no están tomando la referencia global de g, sinó que es una nueva variable local "g", por tanto en todos los llamadas dan 2

## c
### bla

## d
### bla bla