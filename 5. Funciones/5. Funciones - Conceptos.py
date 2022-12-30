# uso del paradigma de programacion secuencial

""" 00:08
# - ¿Qué es una función?

Una funcion es una forma de escribir codigo reutilizable que puede servir para 
utilizarlos mas adelante en otros proyectos o para reducir la complejidad\
del codigo. 

una funcion debe y solo debe realizar una tarea en concreto, al darle un nombre
se debe hacer referencia a lo que haga la funcion.

las funciones en python deben ser escritas antes de ser invocadas ya que el
codigo en python se ejecuta en forma secuencial.

Cuando el interprete invoca a la funcion, se para el programa principal y el 
programa salta hacia la definicion de la funcion invocada, ejecuta todas las 
instrucciones y vuelve a donde estaba antes en el programa principal, esto en
programacion se le llama "Branching" o "Jumping"


"""
def nombre1():
    pass # esta linea se utiliza para indicar que esta pendiente de diseno
    
def mifuncion():
    print("Nombre")
    print("Mas lineas")
    
    for i in range(1,6):
        print("Despues")
        
mifuncion()

"""
# 06:15
# - Parámetros en funciones

Un parametro es una variable que va a ejecutar la funcion, se declara dentro
de la definicion de la [funcion(parametro):] y solo es utilizable dentro del
entorno de la funcion creada.

Los parametos de una funcion se pueden definir como opcionales asignandole un
valor por defecto. Solo deben cumplir con la regla de que todos deben ser
opcionales, o los ultimos.

Python soporta los "named parameters" es decir no importa el orden de los
 argumentos siempre y cuando se especifiquen todos [funcion(p1=a, p2=b):]

Python soporta Parametros variables, es decir que una funcion podria tener 
ninguno o varios parametros [funcion(*args):] *args es una convencion se puede
llamar de cualquier otra forma siempre con el prefijo (*) 
[*args] se convierte en una tupla
"""

def mifuncionP(nombre):
    print("Hola", nombre)
    
mifuncionP("Marco")

#--------------# Funcion con parametro opcional, definido por defecto.

def funcionDef(nombre = "Juan"):
    print(nombre)

funcionDef()

def funcionDefSum(a, b, c=0):
    print(a + b + c)

funcionDefSum(10,5)

#Funcion con "named parameters"

def funcionDefSum2(a, b, c=0):
    print(a + b + c)

funcionDefSum2(b=5, a=5)

# funcion de parametros variables: Tupla de valores

def parVarT(*args):
    resultado = 0
    
    print(args)
    
    for arg in args:
        resultado += arg
        
    print(resultado)
    
parVarT(1,2,3,4,5,0,0,00,0,9)

# funcion de parametros variables: Diccionario

def parVarD(**kwargs):
    
    # iterar un diccionario
    for key, value in kwargs.items():
        print(key, "=", value)
    
parVarD(vivienda="piso", coche="rojo")

#---# Buscar en diccionario [IN] se utiliza para buscar si hay una cosa dentro
#de otra [if [clave] in [diccionario] and [clave]=='valor buscado'
    
def parVarD2(**kwargs):
    
    #compruebo si exixte la clave que busco en mi diccionario
    if 'coche' not in kwargs :
        return # esta palabra reservada hace que salte la funcion
        
    # tambien puedo verificar todo en una linea
    if 'coche' in kwargs and kwargs['coche'] == 'bonito':
           
        print("tu coche es bonito")
        
parVarD2(coche="bonito", coche2="rojo")

""" # - Funciones dentro de funciones 

Las funciones son codigo de python es decir son una caracteristica del lenguaje
de primer nivel, es posible escribir funciones dentro de funciones. 

Las funciones dentro de otra funcion son independientes de la funcion principal
es decir tienen su propio entorno de variables.

"""

def matematicas(a, b):
    def suma(a, b):
        print(a + b)
        
    def resta(a, b):
        print(a - b)    
    
    def masoperaciones(a, b):
        def multiplica (a, b):
            print(a*b)
            
        multiplica(a, b)
    
    suma(a,b)
    resta(a,b)
    masoperaciones(a,b)
    
matematicas(5, 3)

"""# 12:40
# - Variables en funciones

Las variables que se definen en una funcion solamente se pueden utilizar
 dentro de la funcion, una vez que finaliza la funcion, esta variable se borra.
 Desde fuera de la funcion no se puede utilizar la variable de su ambito local
 pero si se pueden utilizar variables globales dentro del entorno local de una 
 funcion.
 
 Cuando tenemos una variable de ambito global con el mismo nombre que una\
local, la que prevalece es la local. a esto se le llama "VARIABLE SHADOWING"
 y no se sobre-escribe la global salvo que se utilice la palabra reservada 
 [global]. En este caso la funcion sobre-escribe a la variable global
"""

hoyHace = 12.0

def mifuncionV(nombre):
    hoyHace = 6.8
    print("Hola", nombre, "La temperatura es de", hoyHace)
#------------#

mifuncionV("Marco")
print(hoyHace)

def mifuncionVG():
    global hoyHace
    hoyHace = 30
    
mifuncionVG()
print(hoyHace)

# El uso tipico de las funciones es retornar valores

def suma3(a,b):
    return a + b

resultado = suma3(2,4)
print(resultado)


#---# funcion que retorna varios valores (TUPLAS)
def operaciones(a,b):
    return a+b,a-b,a*b,a/b

#ahora asigno cada retorno a una variable de forma consecutiva
suma,resta,multi,divi=operaciones(2, 4)

#si necesito solo un valor (multi) e ignorar el resto usar (_) por convencion
_, _, multi, _ = operaciones(2, 4)
print(multi)

# tambien puedo convertir una tupla de los valores retornados
resultados = operaciones(2, 4)
print(resultados)

# mostrar el primer valor retornado de la tupla resultados
print(resultados[0])

#---# funcion que retorna varios valores (DICCIONARIOS)

def sumador(**kwargs):
    inicial = kwargs['inicial']
    final = kwargs['final']
    
    resultado = 0
    for x in range (inicial, final + 1): 
        resultado += x
         
        return resultado
print(sumador(inicial=15,final=30))


#---# funcion que retorna varios valores OPERADOR TERNARIO (DICCIONARIOS)

def sumador2(**kwargs):
    inicial = kwargs['inicial']
    final = kwargs['final'] if 'final' in kwargs else 0
    
    resultado = 0
    for x in range (inicial, final + 1): 
        resultado += x
         
        return resultado
print(sumador(inicial=15,final=30))

"""
# 43:16
# - Funciones lambda o Funciones Anonimas
    se utilizan para disenar funciones mas simples.
    Se diferencian de las funciones normales xq estas no tienen nombre.
    Una funcion anonima es asignada a una variable, pueden tener parametros.
   Las funciones lambda no usan return. hay que indicarselo (ejemplo 2)
    """
anonima = lambda nombre, nombre2: print("Hola!", nombre, "Adios!", nombre2)
anonima("pepe","Maria")

# ejemplo lambda 2
    
sumatoriaL = lambda x:x+x
print(sumatoriaL(2))
