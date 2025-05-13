"""¡Pongámonos a prueba! Teniendo en cuenta la programación modular, intenta resolver:
Escribe un programa para llevar la gestión de usuarios de una aplicación. La misma debe permitir 
registrar usuarios, eliminar y buscar usuarios utilizando módulos. Para ello,
    ● Define un módulo para manejar las operaciones relacionadas con los usuarios.
    ● Define otro módulo para el programa principal que presente un menú para seleccionar la operación 
    y manejar las entradas del usuario."""

# Este es otro comentario de prueba
cuentas = {
    "Juan Perez": {"contraseña": "1234"},
    "Ana Lopez": {"contraseña": "5678"},
    "Carlos Gomez": {"contraseña": "abcd"}
}
# Comentario
def listar_usuarios():
    if not cuentas:
        return "No hay usuarios registrados."
    return list(cuentas.keys())

def buscar_usuario(usuario):
    if usuario in cuentas:
        return f"El usuario '{usuario}' fue encontrado con exito"
    return f"Error: El usuario '{usuario}' no esta registrado. Revisa que lo escribiste correctamente."

def eliminar_usuario(usuario, confirmar):
    if usuario in cuentas:
        if confirmar.lower() == 'si':
            cuentas.pop(usuario)
            return f"El usuario '{usuario}' fue removido con éxito."
        elif confirmar.lower() == 'no':
            return "Operación cancelada."
        else:
            return "Error: respuesta inválida. Escriba 'si' o 'no'."
    return f"Error: El usuario '{usuario}' no fue encontrado."

def registrar_usuario(usuario, contraseña):
    if usuario in cuentas:
        return f"Error: El usuario '{usuario}' ya esta registrado."
    cuentas[usuario] = {"contraseña": contraseña}
    return f"Usuario '{usuario}' registrado correctamente."