"""
Solicitar un texto y realizar lo siguiente:
a. Mostrar uno a uno los caracteres que posee el texto.
b. Indicar cuantos caracteres ‘s’ en mayúscula o minúscula posee.
c. Indicar cuantas vocales posee, ya sea en mayúscula o minúscula.
"""
texto = input("Ingrese un texto: ")
ss=0
vocales=0
for car in texto:
    print(car)
    if car=="s" or car=="S":
        ss=ss+1
    car=car.upper()
    if "AEIOU".find(car)>-1:
        vocales=vocales+1
    
print("El número de s o S en el texto es {}.".format(ss))
print("El número Vocales en el texto es {}.".format(vocales))
