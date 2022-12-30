# Las funciones Built-in son las funciones que ya tiene implementanta python a
# a nivel de interprete, es decir el interprete inyecta la funcion para que se 
# pueda utilizar.

# la python standard library contiene todas las funciones de serie

""" Paradigma de prog. recurrente es cuando se ejecutan muchas instrucciones
 una despues de otra, paradigma de progr. multi hilo es ejecutar varias
 instrucciones al mismo tiempo
 """
import _thread
import time
 
def horaActual(nombre_thread, tiempo_de_espera):
    count = 0 
    while count < 5:
        time.sleep(tiempo_de_espera)
        count += 1
        print(f'Hilo: {nombre_thread} - {time.ctime(time.time())}')
     
# crear una ejecucion multi-hilo, disparo los hilos

_thread.start_new_thread(horaActual, ("thread_uno", 1))
_thread.start_new_thread(horaActual, ("thread_dos", 2))

print("he disparado ya los hilos")

# para que el programa multihilo se ejecute tengo que bloquear el programa
# el programa multihilo no finaliza por si mismo.

while True:
    pass

