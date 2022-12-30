# FUNCION REDUCE: genera un unico resultado a traves de una lista, ejecuta
#ciclicamente la funcion sobre el resultado anterior

from functools import reduce

def suma(a,b):
    print("ESTO ES LO QUE PASA DEBAJO DEL REDUCE", f'a={a}, b={b}')
    return a+b

res = reduce(suma, [1,2,3,4,5])
print(res)
