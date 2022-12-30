# Para este ejercicio tenéis que crear en la consola de python variables que representen los siguientes datos de un contacto:

# Nombre

# Apellidos

# Edad

# Email

# Teléfono

# Casado (verdadero o falso)

# Con Hijos (verdadero o falso)

# Lista de amigos

# Películas vistas (diccionario con clave y valor. El valor será el título de la película)

# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().

# Tienes que subir capturas de pantalla en una carpeta comprimida zip.

nombre = "Teo"
apellido = "Huevo"
edad = "14"
email = "Teo_huevo@python.org"
telefono = "5493543892640"
casado = False
conHij = True
 

listAmig = ["amigo1", "amigo2", "amigo3"]
dictMov = {1:"Scary Movie", 2:"Mr. Bean", 3:"Who is John Galt?", 4: "Alfie 2004"}

print("\n\n")

print(nombre, apellido, "edad:", edad, "Email:", email, "Tel:", telefono, "\n")
print("Es casado?", casado, "Tiene Hijos?", conHij, "\n")
print("Mis amigos son", listAmig, "\n\n", "Nosotros vimos las sig. peliculas:", dictMov)

print("\n END <------------------------------------------------>")
