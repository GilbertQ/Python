#Calcular el sueldo líquido de una persona
# 100 100 100 => 275.34
nombre = input ("Ingrese el nombre del empleado : ")
puesto = input ("Ingrese el puesto de {}: ".format(nombre))
sueldob = input("Ingrese el sueldo base de {}: ".format(nombre))
bonificacion = input("Ingrese el valor de la bonificacion de {}: ".format(nombre))
comisiones = input("Ingrese el valor de las comisiones de {}: ".format(nombre))
sueldoTotal = float(sueldob)+float(bonificacion)+float(comisiones)
ahorro = (sueldoTotal*0.05)
igss = (float(sueldob)+float(bonificacion))*0.0483
sueldoL = sueldoTotal-ahorro-igss
print("El sueldo líquido de {} es: {}.".format(nombre,sueldoL))
