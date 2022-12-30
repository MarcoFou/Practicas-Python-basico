# -*- coding: utf-8 -*-
"""
Clases Abstractas: Sirven para definir un conjunto de funciones comunes a otras
clases

 No se pueden instanciar, hay que derivarla, tengo que disenar la funcion
 concreta para esa determinada clase, que se llama igual pero ejectuta acciones
 concretas de su clase
 
 No se puede instanciar la clase perro con el metodo abstracto sonido porque 
 la clase perro deriva de animal y la clase animal tiene un metodo abstracto 
 tengo que implementar ese metodo a nivel de la clase.
 
 Todos los metodos abstractos deben implementarse en sus subclases heredadas
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sonido(self):
        pass

    #esta funcion no es abstr xq no tiene el encabezado @abstractmethod
    # es decir esta implementacion parcial es general para sus hijas
    def diHola(self):
        print("Hola")
        
class Perro(Animal):
    def sonido(self):
        print("guau")
        
class Gato(Animal):
    def sonido(self):
        print("miau")
        
p = Perro()
p.sonido()
p.diHola()

g =  Gato()
g.sonido()
g.diHola()