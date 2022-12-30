# 34:03
# - Manipulación de ficheros

#la funcion open devuelve una clase a f, que despues la puedo instanciar
# es decir f es una instanciacion, un objeto de open
#la funcion open requiere un permiso

#r: lectura
#a: append
#w: escritura
#x: create

#t: texto
#b: binary

# + 

f = open('C:', 'r')
datos = f.read()


# Leer fichero linea a linea

datos = None

while datos != "":
    datos = f.readline()
    print(datos)

# otra forma

datos = f.readlines() # lo muestra en una lista


#////////////////#
f.close() #cerrar fichero como buena practica