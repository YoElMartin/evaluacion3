import json

def cargar_usuarios():
    try:
        with open("usuarios.json","r") as file:
            usuarios = json.load(file)
            return usuarios
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]
    
def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent = 4)    
def agregar_usuario(nuevo_usuario):
    usuarios = cargar_usuarios()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print(" Usuarios agregado exitosamente. ")
def editar_usuario(id_usuario, nuevo_nombre, nuevo_email, nueva_fecha_registro):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuarios ["id"] == id_usuario:
            usuario ["nombre"] == nuevo_nombre
            usuario ["email"] == nuevo_email
            usuario ["fechaRegistro"] == nueva_fecha_registro
            guardar_usuarios(usuarios)
            print(f"Usuario con id {id_usuario} Editado exitosamente")
            return
        print(f"No se encontro ningun usuario con ID {id_usuario}")
def eliminar_usuario(id_usuario):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            print(F"Usuario encontrado: ")
            print(F"ID: {usuario["id"]}")
            print(F"nombre: {usuario["nombre"]}")
            print(F"email: {usuario["email"]}")
            print(F"Fecha de registro: {usuario["fechaRegistro"]}")
            return
    print(f" No se encontro ningun usuario con ID {id_usuario}.")
