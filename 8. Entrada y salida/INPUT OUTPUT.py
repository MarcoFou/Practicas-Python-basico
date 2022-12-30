""" Descripción

Esta es la octava sesión, donde veremos cómo gestionar las entradas y salidas de un programa.

Puntos clave
"""
# 00:35
# - Formateo de una cadena

numero = 511
texto = "quijote"
otromas = 1.2

# los {} se los llama place-holders y se los rellena en forma ordenada [.format()]
# es como si .format fuera un array y {numero} contiene el numero del elemento del array
print("El numero es {0} y el texto es {1} y tiene {2}"
      .format(numero, texto, otromas))

# otras formas
print("El numero es {n1} y el texto es {m2} y tiene {p3}"
      .format(n1 = 5, m2 = "el huevito", p3 = otromas))

#invocando funciones dentro del print
def suma(a,b):
    return a+b

print(f'El numero SUMA es {suma(numero,numero)} y el texto es {texto.upper()} y tiene {otromas}')

txt = f'El numero SUMA es {suma(numero,numero)} y el texto es {texto.upper()} y tiene {otromas}'
print(txt)



# 14:28
# - Representaciones textuales de una clase

print(type(numero))

numtxt = str(numero)
print(" ejemplo STR: SE USA PARA SALIDAS INFORMALES PARA EL USU FINAL Y DESCRIPCIONES",type(numtxt))

print("EJEMPLO REPR SE SA PARA SALIDAS DE DEPURACION Y DESARROLLO", type(repr(numero)))

#----------# 
class Juguete:
    nombre = ""
    precio = 0.0
    
    #Constructor
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    #este metodo sirve para mostrar al desarrollador lo que muestra class
    # es sobrecarga del metodo __str__
    
    def __str__(self):
        return(f'mi nombre es {self.nombre} y mi precio es {self.precio}')
    
    def __repr__(self):
        return f"huevito {self.nombre}, {self.precio}"
    
    def __repr__(self):
        return self.__str__()
        
j1 = Juguete("huevito", 5000)

print(type(j1))

print(j1)

j1txt = str(j1)

print(type(j1))

print(repr(j1))

    
# 25:33
# - Métodos en las cadenas de texto

""" paraa ver los metodos que existen para las cadenas de texto """
import pprint

pprint.pprint(dir(""))

cadena = "En un lugar de la mancha"
print(cadena.title())

# se puede utilizar la salida de una funcion en la misma linea y aplicar otra f.
print(cadena.lower().count('a'))

# verificar si una variable es un numero
numero = "5"
print(numero.isdigit())

# quitar espacios de la derecha e izquierda de una una cadena

cadena2 = "           el huevitooo               .         "
print(cadena2.lstrip())
print(cadena2.rstrip())

#dividir cadena
print(cadena2.split('el'))

# verificar si termina en 
print(cadena2.endswith('huevitooooo'))


