# Funcion zip: agrega iterables en una tupla y los devuelve.
#devuelve una lista, cada elemento es una tupla, sirve para asociar elementos

cursos = ['java', 'python', 'gyt']
asistentes = [15, 20, 4]
demo = zip(cursos, asistentes)
print(list(demo))