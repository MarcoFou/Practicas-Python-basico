secreto = 50
valor = 0

while valor != secreto:
    valor = int(input("introduce un numero"))
  # valor = int(valor)
    
    if valor > secreto:
        print('muy alto')
        continue
    if valor < secreto:
        print('muy bajo')
        continue
    
print("acertaste")
    
valor = int(input("introduce un numero: "))
