import modules.core as cr
import modules.utils as ut

def agregar_contacto(lista_contactos):
    
    ut.borrar_pantalla()

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

    lista_contactos[nombre] = contacto # Agrega el nuevo contacto al diccionario de la lista de contactos

    cr.AddData(lista_contactos)

    print("Contacto agregado exitosamente.")
    print(f"Contacto agregado: {nombre} {apellido}, Teléfono: {telefono}, Correo: {correo}")
    ut.pausar_pantalla()

def mostrar_contactos(lista_contactos):
    ut.borrar_pantalla()
    print("Lista de contactos:")
    for nombre, contacto in lista_contactos.items():
        print(f'{nombre} {contacto["apellido"]} - {contacto["telefono"]} - {contacto["correo"]}')

def buscar_contacto(lista_contactos):
    print("Buscar contacto")

def actualizar_contacto(lista_contactos):
    print("Actualizar contacto")

def eliminar_contacto(lista_contactos):
    print("Eliminar contacto")