# -*- coding: utf-8 -*-
"""
Composiciones: una clase esta compuesta.

La diferencia entre compocision y herencia esta en que en la composicion 
una clase tiene una o mas instancias de otras clases yu no heredan funciones.
se pueden mezclar composiciones y herencias, se recomenda usar composiciones.

las clases deben estar instanciadas antes de ser invocadas, es secuencial.

"""
class Motor:
    tipo = "Diesel"

class Ventanas:
    cantidad = 5
    def cambiarCantidad(self, valor):
        self.cantidad = valor

class Ruedas:
    cantidad = 4
    
class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()
    
c = Coche()

# lectura
print("Motor es", c.motor.tipo)
print("ventanas:", c.carroceria.ventanas.cantidad) 

#escritura
c.carroceria.ventanas.cambiarCantidad(3)

print("ventanas:", c.carroceria.ventanas.cantidad) 