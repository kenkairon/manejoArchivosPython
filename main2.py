import os

# Función para guardar más de un conjunto de datos en el archivo
def guardar_datos():
    while True:
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")

        # Agregar datos al archivo sin sobrescribir los existentes
        with open("datos_usuario.txt", "a") as archivo:
            archivo.write(f"{nombre},{edad}\n")  # Guardamos en formato CSV

        print("Datos guardados en 'datos_usuario.txt'.")

        # Preguntar si quiere agregar otro usuario
        continuar = input("¿Desea agregar otro usuario? (si/no): ").strip().lower()
        if continuar != "si":
            break

# Función para leer los datos desde el archivo
def leer_datos():
    if os.path.exists("datos_usuario.txt"):
        with open("datos_usuario.txt", "r") as archivo:
            usuarios = archivo.readlines()
            if usuarios:
                print("\nDatos actuales:")
                for i, usuario in enumerate(usuarios):
                    nombre, edad = usuario.strip().split(",")
                    print(f"{i + 1}. Nombre: {nombre}, Edad: {edad}")
            else:
                print("No hay datos guardados.")
    else:
        print("No hay datos guardados.")

# Función para eliminar datos de un usuario específico
def eliminar_datos():
    if os.path.exists("datos_usuario.txt"):
        with open("datos_usuario.txt", "r") as archivo:
            usuarios = archivo.readlines()

        if not usuarios:
            print("No hay datos para eliminar.")
            return

        print("\nDatos actuales:")
        for i, usuario in enumerate(usuarios):
            nombre, edad = usuario.strip().split(",")
            print(f"{i + 1}. Nombre: {nombre}, Edad: {edad}")

        try:
            seleccion = int(input("\nIngrese el número del usuario que desea eliminar: ")) - 1
            if 0 <= seleccion < len(usuarios):
                # Confirmar la eliminación
                confirmacion = input(f"¿Está seguro de que desea eliminar a {usuarios[seleccion].strip()}? (si/no): ").strip().lower()
                if confirmacion == "si":
                    usuarios.pop(seleccion)  # Eliminar el usuario seleccionado

                    # Reescribir el archivo con los datos restantes
                    with open("datos_usuario.txt", "w") as archivo:
                        archivo.writelines(usuarios)

                    print("Usuario eliminado.")
                else:
                    print("Operación cancelada.")
            else:
                print("Selección inválida.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    else:
        print("No hay datos para eliminar.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú Mantenedor ---")
        print("1. Crear/Guardar Datos")
        print("2. Leer Datos")
        print("3. Eliminar Datos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            guardar_datos()
        elif opcion == "2":
            leer_datos()
        elif opcion == "3":
            eliminar_datos()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú
menu()
