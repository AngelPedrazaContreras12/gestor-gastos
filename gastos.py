def mostrar_menu():
     print("\n=== GESTOR DE GASTOS ===")
print("1. Agregar gasto")
print("2. Ver gastos")
print("3. Resumen por categoria")
print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            print("Aquí vamos a agregar un gasto")
        elif opcion =="2":
            print("Aquí vamos a ver los gastos")
        elif opcion =="3":
            print("Aquí vamos a ver el resumen")
        elif opcion=="4":
            print("¡Hasta luego!")
            break
        else:
            print("Opcion no válida, intente de nuevo")


    main()