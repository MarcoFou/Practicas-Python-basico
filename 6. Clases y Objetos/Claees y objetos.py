# uso del paradigma de programacion orientada a objetos
"""
00:46
- ¿Qué es un objeto?
02:36
&&
- ¿Cómo se crea una clase en Python?


Un objeto es una representacion en un lenguaje de algo real, estos objetos 
tienen metodos que manipulan al objeto y propiedades que pueden mutar.

craecio de un objeto: Los objetos consisten en instanciar a una clase que
 implementa el objeto.
 
 Crear una instancia significa crear un objeto.
 Crear un objeto significa instanciar una clase.
 
 las funciones dentro de una clase se conocen como metodos 
 
 no es necesario de clarar las variables antes de usarlas
 
 En Python NO EXISTE el concepto de PUBLIC, PRIVATE y  PROTECTIVE. por def
 es Public.
 Hay una convencion que dice que si una propiedad o funcion empieza con _ No se
 deberia modificarl el valor de esa propiedad, i se puede pero no se deberia
 
 Cuando se modifica una variable o propiedad dentro de una clase,para 
 hacer referencia a la variable o propiedad de la clase, hay que anteponer 
 [self.] si no escribo esto de antemano, estoy creando una nueva variable local

Cuando creo una instancia, s ereserva una zona de memoria para esa clase
pero es particular de cada objeto.

# Las clases en python no existen, sino que son diccionarios disfrazados
de clases 00:40:20
"""

class Juguete:
    _encendido = True
    
    def enciende(self):
        self._encendido = True
    
    def apaga(self):
       self._encendido = False
       
    def isEncendido(self):
        return self._encendido
        
# Creo el objeto d (una instancia de mi clase Dino) contiene todos los metodos de la clase Dino()
d1 = Juguete()
d1.enciende()
print(d1.isEncendido())

# 14:45
# - Clases estáticas: Las clases estaticas son como las dinamicas solo que comparten todo
#como cartacteristica no contienen el parametro [self.]
# Se utilizan para hacer enumeraciones o opciones
# No pueden tener multiples instancias

class Estatica:
    numero = 1
    
    def incrementa():
        Estatica.numero+=1

Estatica.incrementa()
print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)


#ejemplo 2 

class Opciones:
    ServidoSeguro = True 
    Reiniciar = False
    
# if Opciones.ServidoSeguro:
#     codigo[...]

# 19:32
# - Herencia: Consiste en que una clase hereda las propiedades y los metodos
# de otra clase base. en el ejemplo MiClase hereda las caracteristicas 
# de Juguete


class Potato(Juguete):

    def ponerOreja(self):
        pass
    
# ejemplo herencia multiple, se debe hacer de menor a mayor
# es decir de abajo hacia arriba (potato esta despues que juguete)

    
# 30:40
# - Constructor: el instanciar una clase se le llama constructor 
# Los constructores sirven para cambiar el estado de las clases.
# Los constructores solo se disparan cuando instanciamos una clase.
# Cuando se instancia la clase, los parametros que se escriben 
# son del constructor (dentro de la funcion __init__ )

class Dino(Potato, Juguete):

    color = None
    nombre = None
    
    def __init__(self, nombre):
        
        print("estoy en el constructor", nombre)
        self.color = "verde"
        self.nombre = nombre

    def verEscamas(self):
        pass


# Ver funciones heredadas de una clase particular [dir.(p)]

p = Dino("midinosaurito")
print(dir(p))

q = Dino("midinosaurito")
print(q.nombre)
print(q.color)

# Para invocar el constructor de la clase base superior, se usa el metodo Super

class Dino2(self,nombre):
    super().__init__()
    print("estoy en el constructor de la clase Dino2")
    
# Otra forma de hacer lo mismo
class Dino3(self,nombre):
    Juguete.__init__(self, nombre)
    print("estoy en el constructor de la clase Dino3")


# 33:09
# - Destructores: en python no son necersarios pero en c++ se utilizan
# para liberar memoria, se invocan automaticamente cuando no existen mas 
# referencias a estas clases.
# Mostrar nombre de la clase [__class__]

def __del__(self):
    print("estoy en el destructor de la clase", self.__class__)

# Para forzar la ejecucion del destructor
print("a")
del(p)
print("b")


# 44:07
# - Clase abstractas





# 49:22
# - Relaciones HAS-A