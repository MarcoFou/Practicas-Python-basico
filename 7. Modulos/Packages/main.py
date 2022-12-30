"""
Cuando importo un paquete tengo que importar 
los modulos que voya a usar

tambien se puede usar import operaciones.suma

al invocar una funcion se hace referencia a:
    [nombre del paquete].[nombre del modulo].[funcion]
es como una jerarquia de afuera hacia adentro
"""

#import pprint
import sys 
sys.path.append("F:/Programacion/OpenBootcamp/Python/7. Modulos/ Packages")

import pprint
import operaciones2.restador.resta
import operaciones2.sumador.suma
#from operaciones2 import sumador, restador


#en el fichero __init__ puedo especificar que modulos quiero importar con el *


def main():
    
    mp = operaciones2.sumador.suma.Multiplicador()
        
    print(operaciones2.sumador.suma.suma(2,2))
    print(mp.multiplica(5,5))
   
#    pprint.pprint(sys.path)

# FUNCION DIR: MUESTRA LOS METODOS Y ATRIBUTOS QUE CONTIENE UN OBJETO,
# VARIABLES, LO QUE SEA EN PYTHON CASI TODO ES UN OBJETO

#pprint.pprint(dir(mp))
pprint.pprint(dir("A"))
pprint.pprint(dir((tupla))
pprint.pprint(dir(0.02))

if __name__ == "__main__":
    main()