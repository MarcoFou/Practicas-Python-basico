# -*- coding: utf-8 -*-
"""

"""
class Categorias:
        idCategoria = 0
        nombre = ""
class Proveedores:
     idProveedor = 0
     nombre = 0
     
class Productos:
    idProducto = 0
    categoriaProducto = Categorias()
    precio = 0
    tamano = 0
    tipoDeProducto = 0
    cifProveedor = Proveedores()
          
   
           
p = Productos()
p.cifProveedor.nombre