
print('Ingresar la frase')
frase = input().lower()

palabras = frase.split()

print('Ingrese la cadena a buscar')
cadena =input().lower()


print(palabras.count(cadena))