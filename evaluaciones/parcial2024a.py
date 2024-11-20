from queue import Queue as Cola
"""ACLARACIONES :: 
aclaraciones este parcial NO ESTA PERFECTO, lo subo para aportar a la comunidad, la nota fue de 9.28 los ejercicios que generan conflicto son el 3 y el 4 en este ultimo el error es que no considero el caso
en el que el registro esta vacio y hago una division por 0, y en el 3 el problema es cuando la matriz es de 6*6 
"""

"""
1) Alerta Enfermedades Infecciosas (3 puntos)

Necesitamos detectar la aparición de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los registros de atención por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad que motivó la atención. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporción de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

problema alarma_epidemiologica (registros: seq⟨ZxString⟩, infecciosas: seq⟨String⟩, umbral: R) : dict⟨String,R⟩ {
  requiere: {0 < umbral < 1}
  asegura: {claves de res pertenecen a infecciosas}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de e pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}
}
"""

T = type

def mi_in (lista: list[T], e: T) -> bool:
    for elm in lista:
        if elm == e:
            return True
    return False


def alarma_epidemiologica (registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    res_dict : dict[str, float]
    total_pacientes: int = 0
    
    for tlp in registros:
        total_pacientes += tlp[0]
    
    for tlp in registros:
        if mi_in(infecciosas, tlp[1]) and (tlp[0] / total_pacientes) >= umbral:
            res_dict[tlp[1]] = tlp[0] / total_pacientes
    
    return res_dict
            
        

"""
2) Orden de atención (1 punto)

Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la información que maneja sobre los pacientes y el personal de salud. 
En primer lugar debemos resolver en qué orden se deben atender los pacientes que llegan a la guardia. 
En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable (esto se llama hacer triage). 
A partir de dichas colas que contienen la identificación del paciente, se pide devolver una nueva cola según la siguiente especificación.

problema orden_de_atencion ( in urgentes: cola⟨Z⟩, in postergables: cola⟨Z⟩) : cola⟨Z⟩ {
  requiere: {no hay elementos repetidos en urgentes}
  requiere: {no hay elementos repetidos en postergables}
  requiere: {la intersección entre postergables y urgentes es vacía}
  requiere: {|postergables| = |urgentes|}
  asegura: {no hay repetidos en res }
  asegura: {res es permutación de la concatenación de urgentes y postergables}
  asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
  asegura: {En res no hay dos seguidos de urgentes}
  asegura: {En res no hay dos seguidos de postergables}
  asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res}
  asegura: {Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res}
"""

def devolver_lista (cola: Cola[T]) -> list[T]:
    res_lista: list[T] = []
    while not cola.empty():
        res_lista.append(cola.get())
    for elm in res_lista:
        cola.put(elm)

def orden_de_atencion (urgentes: Cola[int], postrgables: Cola[int]) -> Cola[int]:
    handler_urg_list: list[int] = devolver_lista(urgentes)
    res_cola: Cola[int] = Cola()
    posicion: int = 0
    for elm in devolver_lista(postrgables):
        handler_urg_list.insert((1*posicion)+1, elm)
    
    for elm in handler_urg_list:
        res_cola.put(elm)
    return res_cola

"""
3) Camas ocupadas en el hospital (2 puntos)
Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en donde las filas son los pisos, y las columnas son las camas. Los valores de la matriz son booleanos que indican si la cama está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada. Se nos pide programar en Python una función que devuelve una secuencia de enteros, indicando la proporción de camas ocupadas en cada piso.

problema nivel_de_ocupacion(camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
  requiere: {Todos los pisos tienen la misma cantidad de camas.}
  requiere: {Hay por lo menos 1 piso en el hospital.}
  requiere: {Hay por lo menos una cama por piso.}
  asegura: {|res| = |camas|}
  asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)}
}
"""
def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
    res_list: list[float] = []
    
    for piso in camas_por_piso:
        cant_camas : int = 0
        cant_camas_ocu: int = 0
        for cama in piso:
            cant_camas+=1
            if cama:
                cant_camas_ocu+=1
        res_list.append(cant_camas_ocu/cant_camas)
    return res_list

"""
4) Quiénes trabajaron más? (2 puntos)
Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es una lista de las horas trabajadas por día, queremos saber quienes trabajaron más para darles un premio. Se deberá buscar la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.

problema empleados_del_mes(horas:dicc⟨Z,seq⟨Z⟩⟩) : seq⟨Z⟩ {
  requiere: {No hay valores en horas que sean listas vacías}
  asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
  asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
  asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}
}


}
"""
def cant_horas(lista: list[int]) -> int:
    res: int = 0
    for val in lista:
        res+=val
    return res

def empleados_del_mes(horas:dict[int, list[int]]) -> list[int]:
    emp_del_mes : tuple[int, int] = (0,0)
    for emp in horas.items():
        emp_horas: int = cant_horas(emp[1])
        if emp_del_mes[1] < emp_horas:
            emp_del_mes = (emp[0], emp_horas)
    
    
    