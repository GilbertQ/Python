"""
Solicitar el ingreso de usuario y contraseña y realizar lo siguiente:
a. Si el usuario y contraseña son válidos (usuario = aprendiendo, contraseña =
Python), deberá dar la bienvenida.
b. Si los datos son incorrectos deberá volver a solicitar el ingreso de los datos.
c. Al alcanzar 5 intentos fallidos deberá mostrar el mensaje que la aplicación
finalizará por seguridad.
"""
intento=0
while True:
    usuario = input("Ingrese el usuario: ")
    passw = input("Ingrese la contraseña: ")
    if usuario=="aprendiendo" and passw=="Python":
        print("Bienvenido al módulo")
        intento=5
    else:
        intento=intento+1
    if intento>4:
        if usuario!="aprendiendo" and passw!="Python":
            print("Alcanzó el límite de intentos fallidos: 5. Adios")
        break
