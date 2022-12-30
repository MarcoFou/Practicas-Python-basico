# Funcion filter: EXTRAE LOS RESULTADOS DE UNA LISTA (itera sobre ella) CUANDO
# SE CUMPLE EL TRUE DE LA FUNCION

numeros = [1,2,3,4,5,6,7,8,9,10]

#devolver numeros pares
def mifuncion(x):
    
    if x % 2 == 0:
        return True
    
    return False
    
    
resultado = filter(mifuncion, numeros)

print(list(resultado))



#//////////# otra forma usando lambdas

resultadoL = filter(lambda x: x % 2, numeros)

print(list(resultadoL))

# hacer un buscador con filter

def funcionBuscador(x):
    if str(x).startswith('pep'):
        return True
    
    return False


buscador = filter(funcionBuscador, ['pepe', 'pepito', 'juan']) 
print(list(buscador))


# hacer un buscador utilizando lambdas

buscadorL = filter(lambda x: str(x).startswith('pep'), ['pepe', 'pepito', 'juan'])
print(list(buscadorL))
