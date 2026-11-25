from datetime import date


def mostrar_menu():
    print("\n=== GESTOR DE GASTOS ===")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Resumen por categoria")
    print("4. Salir")


def agregar_gasto(gastos):
    descripcion = input("Descripcion: ")
    categoria = input("Categoría (Comida, Transporte, Escuela, Otros): ")

    try:
        monto = float(input("Monto: $"))
    except ValueError:
        print("El monto debe de ser un número. No se guardó el gasto.")
        return

    gasto = {
        "fecha": str(date.today()),
        "descripcion": descripcion,
        "categoria": categoria.capitalize(),
        "monto": monto,
    }
    gastos.append(gasto)
    print("Gasto agregado correctamente.")


def ver_gastos(gastos):
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return

    print("\n--- LISTA DE GASTOS ---")
    for gasto in gastos:
        print(f"{gasto['fecha']} | {gasto['categoria']} | {gasto['descripcion']} | ${gasto['monto']:.2f}")


def main():
    gastos = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            agregar_gasto(gastos)
        elif opcion == "2":
            ver_gastos(gastos)
        elif opcion == "3":
            print("Aquí vamos a ver el resumen")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opcion no válida, intente de nuevo")


if __name__ == "__main__":
    main()