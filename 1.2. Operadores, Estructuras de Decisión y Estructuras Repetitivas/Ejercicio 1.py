import os
os.system("cls")

def agregar():
    print("Agregar contacto")
    nombre = input("Ingrese el nombre del contacto: ")
    apellido = input("Ingrese el apellido del contacto: ")
    telefono = int(input("Ingrese el número de teléfono del contacto: "))
    correo = input("Ingrese el correo electrónico del contacto: ")
    contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "correo": correo
    }
    lista_contactos.append(contacto)
    print(f"Contacto agregado: {nombre} {apellido}, Teléfono: {telefono}, Correo: {correo}")

print("Bienvenido a la agenda de contactos")

lista_contactos = []
isActive = True

while isActive:
    opcion = int(input("Seleccione la operación a realizar: \n1. Agregar contacto\n2. Buscar contacto\n3. Actualizar contacto\n4. Eliminar contacto\n0. Salir\n"))

    match opcion:
        case 1:
            agregar()
        case 2:
            print("Buscar contacto")
            print(lista_contactos)
        case 3:
            print("Actualizar contacto")

        case 4:
            print("Eliminar contacto")
        case 0:
            print("Gracias por usar la agenda de contactos. ¡Hasta luego!")
            isActive = False
        case _:
            print("Selección inválida. Intente nuevamente.")
