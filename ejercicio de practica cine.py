
print("Bienvenido al Cine")

edad = input("Ingrese la edad del cliente: ")

if edad.isnumeric():
    if int(edad) < 4:
        print("La entrada es gratis!")
    elif int(edad) in range(4,19):
        print("La entrada cuesta 10$")
    else:
        print("La entrada cuesta 14$")

else:
    print("Ingreso invalido")