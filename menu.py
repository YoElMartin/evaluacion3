def MostrarMenu():
    print("***************\n Mundo libro \n***************")

    print("[1], Mantenedor de usuarios")
    print("[2], Reportes")
    print("[3], Salir")
def main():
    while True:
        MostrarMenu()
        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            print("Seleccione Mantenedor de usuarios")
        elif opcion == "2":
            print("Seleccione Reportes")
        elif opcion == "3":
            print(" Saliendo del programa")
            break
        else:
            print("Opcion no valida, eliga nuevamente otra opcion")

