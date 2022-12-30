
"""
00:10
- ¿Qué es un módulo?
00:35
- ¿Para qué sirven los módulos?
02:07
- Creando un módulo
02:50
- Ejecutando un módulo
04:20
- ¿Cómo saber el nombre de los módulos?
08:00
- Creando más módulos
10:48
- Importando módulos
12:20
- Acortando nombre de los modulos en el import
18:35
- Importando módulos Python
24:34
- Package
54:00
- Ámbitos


Los modulos en python se deben importary y para usar sus funciones se deben 
hacer referencia primero al nombre del modulo o a su alias. 

    al disenar un modulo tener en cuenta que no es mas que codigo python que se
ejecuta en el programa principal , en la mayoria de los casos los mmodulos solo
se componen de clases y funciones, en raras ocaciones de codigo del ambito
global
"""

import sys as sys
sys.path.append("C:/Users/Admin/hhh")
import saluda as sal
import pprint as pprint 
import operaciones as o



def main():
    
    print("Hola en main")
    
    # invoco una constante global del modulo operaciones
    
    # invoco una funcion global del modulo operaciones
    res = o.suma(2,2)
    print("Resultado de mi funcion del mod operaciones", res)
    
    # invoco una clase del modulo operaciones
    op = o.Operador()
    print("resultado de multiplicacion",op.multiplicacion(4,2))
   

    print("el modulo usado se llama", o.como_me_llamo())

 # Ver el path del modulo utilizado (rutas donde busca los modulos invocados)
    
    pprint.pprint(sys.path)

# puedo invocar modulos de cualquier directorio cambiando la variable path
# como sys.path es una List puedo usar la funcion append para anadirla.

# como python es secuencial antes de importar el nuevo path primero debo
# anadirle arriba de todo la ruta del modulo que estoy por usar

#-----# sys.path.append("C:/Users/Admin/hhh>")

# Invoco el modulo personalizado
sal.saluda("Fouad")
sal.saluda("Victor")


#                           PAQUETES 

# Los modulos se agrupan en paquetes, que son una coleccion de modulos
# y paquetes. 

# Un paquete en python es un directorio con un fichero especial adentro



if __name__ == '__main__':
    main()
    