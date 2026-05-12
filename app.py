import modules.core as cr
import modules.utils as ut
import modules.contacts as ct
import modules.messages as ms

if __name__ == "__main__":

    origin = {} # Variable para almacenar los contactos
    cr.MY_DATABASE = "data/agenda.json" # Ruta del archivo de la base de datos
    cr.CheckFile(origin) # Verifica si el archivo de la base de datos existe, si no, lo crea

    print("Bienvenido a la agenda de contactos")
    isActive = True

    while isActive:
        try:
            ut.borrar_pantalla()
            opcion = int(input(ms.menu_principal))

            match opcion:
                case 1:
                    ct.agregar_contacto(origin)
                case 2:
                    ct.mostrar_contactos(origin)
                    ut.pausar_pantalla()
                case 3:
                    ct.buscar_contacto(origin)
                case 4:
                    ct.actualizar_contacto(origin)
                case 5:
                    ct.eliminar_contacto(origin)
                case 0:
                    print("Gracias por usar la agenda de contactos. ¡Hasta luego!")
                    isActive = False
                case _:
                    print("Selección inválida. Intente nuevamente.")
                    ut.pausar_pantalla()
        except:
            print("Error al ingresar los datos, debe ser un numero entero.")
            ut.pausar_pantalla()