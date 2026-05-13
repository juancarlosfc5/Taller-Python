import modules.core as cr
import modules.utils as ut

def agregar_contacto(lista_contactos):
    
    ut.borrar_pantalla()

    print("Agregar contacto")
    nombre = input("Ingrese el nombre del contacto: ").lower()
    apellido = input("Ingrese el apellido del contacto: ").lower()
    telefono = int(input("Ingrese el número de teléfono del contacto: "))
    correo = input("Ingrese el correo electrónico del contacto: ").lower()
    
    contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "correo": correo
    }

    lista_contactos[nombre] = contacto # Agrega el nuevo contacto al diccionario de la lista de contactos

    cr.AddData(lista_contactos)

    print("Contacto agregado exitosamente.")
    print(f"Contacto agregado: {nombre} {apellido}, Teléfono: {telefono}, Correo: {correo}")
    ut.pausar_pantalla()

def mostrar_contactos(lista_contactos):
    ut.borrar_pantalla()
    print("Lista de contactos:")
    for i, (nombre, contacto) in enumerate(lista_contactos.items()):
        print(f'{i+1}. {nombre} {contacto["apellido"]} - {contacto["telefono"]} - {contacto["correo"]}')

def buscar_contacto(lista_contactos):
    ut.borrar_pantalla()
    print("Buscar contacto")
    nombre = input("Ingrese el nombre del contacto a buscar: ").lower()
    if nombre in lista_contactos:
        contacto = lista_contactos[nombre]
        print(f'Contacto encontrado: {nombre} {contacto["apellido"]} - {contacto["telefono"]} - {contacto["correo"]}')
        ut.pausar_pantalla()
        return nombre
    else:
        print("Contacto no encontrado.")
        ut.pausar_pantalla()

def actualizar_contacto(lista_contactos):
    nombre = buscar_contacto(lista_contactos)
    ut.borrar_pantalla()
    print("Actualizar contacto")
    new_nombre = input("Ingrese el nuevo nombre del contacto: ").lower()
    new_apellido = input("Ingrese el nuevo apellido del contacto: ").lower()
    new_telefono = int(input("Ingrese el nuevo número de teléfono del contacto: "))
    new_correo = input("Ingrese el nuevo correo electrónico del contacto: ").lower()
    
    new_contacto = {
        "nombre": new_nombre,
        "apellido": new_apellido,
        "telefono": new_telefono,
        "correo": new_correo
    }

    lista_contactos[nombre] = new_contacto # Agrega el nuevo contacto al diccionario de la lista de contactos

    cr.AddData(lista_contactos)

    print("Contacto actualizado exitosamente.")
    ut.pausar_pantalla()

def eliminar_contacto(lista_contactos):
    ut.borrar_pantalla()
    print("Eliminar contacto")
    nombre = input("Ingrese el nombre del contacto que quiere eliminar: ").lower()

    if nombre in lista_contactos:
        lista_contactos.pop(nombre)
        print("Contacto eliminado")
        cr.AddData(lista_contactos)
        ut.pausar_pantalla()
    else:
        print("El contacto no existe")
        ut.pausar_pantalla()