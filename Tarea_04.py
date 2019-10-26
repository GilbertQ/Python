"""
Solicitar un texto y realizar lo siguiente:
a. Mostrar la cantidad de caracteres que posee.
b. Mostrar el primer y último carácter.
c. Indicar si el primer carácter es una vocal o no.
"""
vocales="AEIOU"
texto = input("Ingrese un texto: ")
print("El texto ingresado contiene {} caracteres".format(len(texto)))
print("El primer caracter es {} y el último es {}.".format(texto[0],texto[len(texto)-1]))
first=texto.upper()
if vocales.find(first[0])>-1:
    print("El primer caracter = {}, es una vocal".format(texto[0]))
else:
    print("El primer caracter = {}, No es una vocal".format(texto[0]))
        
