import csv
import os
from datetime import date

ARCHIVO = "gastos.csv"

def mostrar_menu():
    print("\n=== GESTOR DE GASTOS ===")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Resumen por categoria")
    print("4. Salir")

def cargar_gastos():
    if not os.path.exists(ARCHIVO):
        return []

    gastos = []
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila["monto"] = float(fila["monto"])
            gastos.append(fila)
    return gastos


def guardar_gastos(gastos):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        campos = ["fecha", "descripcion", "categoria", "monto"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(gastos)

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


def resumen_por_categoria(gastos):
    if len(gastos) == 0:
        print("No hay gastos registrados.")
        return

    totales ={}
    for gasto in gastos:
        categoria = gasto["categoria"]
        if categoria in totales:
            totales[categoria] += gasto["monto"]
        else:
            totales[categoria] = gasto["monto"]

    print("\n--- RESUMEN POR CATEGORIA ---")
    for categoria, total in totales.items():
        print(f"{categoria}: ${total:.2f}")


    total_general = sum(totales.values())
    print(f"TOTAL: ${total_general:.2f}")


def main():
    gastos = cargar_gastos()
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            agregar_gasto(gastos)
            guardar_gastos(gastos)
        elif opcion == "2":
            ver_gastos(gastos)
        elif opcion == "3":
            resumen_por_categoria(gastos)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opcion no válida, intente de nuevo")


if __name__ == "__main__":
    main()