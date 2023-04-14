texto = """El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas."""

mayusculas = 0
minusculas = 0
no_letras = 0

for letra in texto:
    if letra.isalpha():
        if letra.islower():
            minusculas+=1
        else:
            mayusculas+=1
    else:
        no_letras+=1

palabras = texto.split()

print('Mayusculas:',mayusculas,' Minusculas:',minusculas,' Caracteres no alphabeticos;',no_letras)
print('Cantidad de palabras:',len(palabras))