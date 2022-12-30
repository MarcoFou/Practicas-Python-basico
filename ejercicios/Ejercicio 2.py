# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura 
# (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por
#  pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado 
#  redondeado con dos decimales. Tienes que subir capturas de pantalla en una carpeta comprimida zip.

peso = input("¿Cuál es tu peso en kg?  86") ## Pedimos el peso al usuario

estatura = input("¿Cuál es tu estatura en metros?  ") ## Pedimos la altura al usuario

imc = round(float(peso)/float(estatura)**2,2) ## Calculamos el índice de masa corporal truncado a 2 decimales

print("Tu índice de masa corporal es " + str(imc))