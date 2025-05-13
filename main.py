import usuarios

def menu():
        print("Menu de gestion de usuarios")
        print("1. Registrar nuevo usuario")
        print("2. Eliminar usuario existente")
        print("3. Buscar usuario existente")
        print("4. Listar usuarios")
        print("5. Salir del programa")

def main():
        while True:
            menu()
            opcion = input("Seleccione una de las opciones: ")

            if opcion == '1':
                usuario = input("Ingrese el nombre de usuario: ")
                contraseña = (input("Ingrese la contraseña: "))
                print(usuarios.registrar_usuario(usuario, contraseña))

            elif opcion == '2':
                usuario = input("Ingrese el usuario que quiere eliminar: ")
                confirmar = input(f"¿Esta seguro que decea eliminar al usuario '{usuario}'? si/no: ")
                print(usuarios.eliminar_usuario(usuario, confirmar))

            elif opcion == '3':
                usuario = input("Ingrese el nombre del usuario a buscar: ")
                print(usuarios.buscar_usuario(usuario))

            elif opcion == '4':
                print("Usuarios registrados:")
                for registrados in usuarios.listar_usuarios():
                    print(f"- {registrados}")

            elif opcion == '5':
                print("Saliendo del programa.")
                break
            elif opcion == '6':
                 print("Erro")
            else:
                print("Error: Seleccione una opcion valida (1, 2, 3, 4, 5)")

if __name__ == "__main__":
    main()