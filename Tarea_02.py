#Solicitar el ingreso de 1 valor numérico entero e indicar si este es múltiplo de 7 y es par.

valor=input("Ingrese un valor numérico: ")
if int(valor)>7:
    multip7 = int(valor)%7
else:
    multip7=1
par = int(valor)%2
if multip7==0 and par ==0:
    print("{} es múltiplo de 7 y par.".format(valor))
elif multip7==0:
    print("{} es múltiplo de 7.".format(valor))
elif par ==0:
    print("{} es par.".format(valor))
else:
    print("{} no es múltiplo de 7 ni par.".format(valor))
