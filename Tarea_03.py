"""
Solicitar el ingreso de 3 valores numéricos enteros
y con ellos realizar lo siguiente:
a. Elevar el primer valor al cubo.
b. Multiplicar el segundo por el tercero.
c. Indicar si el resultado de la primera operación es mayor, menor o igual a la
anterior.
"""
valor1 = input("Ingrese el primer valor: ")
valor2 = input("Ingrese el segundo valor: ")
valor3 = input("Ingrese el tercer valor: ")
cubo=int(valor1)**3
multiplica=int(valor2) * int(valor3)
if cubo>multiplica:
    print("La primera operación es mayor: {} es mayor que {}.".format(cubo,multiplica))
elif cubo<multiplica:
    print("La primera operación es menor: {} es menor que {}.".format(cubo,multiplica))
else:
    print("Ambas operaciones son iguales: {} es igual que {}.".format(cubo,multiplica))    
