print('Ingrese una palabra')
palabra = input().lower()
letras = {}

for letra in palabra:
    if not (letra in letras):
        letras[letra] = 0


if len(letras) == len(palabra):
    print('La palabra es Heterograma')
else:
    print('La palabra no es Heterograma') 