# 💰 Gestor de Gastos

Aplicación de consola en Python para registrar gastos personales, verlos y obtener un resumen por categoría. Los datos se guardan en un archivo CSV para que no se pierdan al cerrar el programa.

## Funcionalidades
- Agregar gastos con descripción, categoría y monto (la fecha se registra automáticamente)
- Ver la lista de todos los gastos
- Resumen del total gastado por categoría y total general
- Guardado automático en `gastos.csv`
- Validación de montos inválidos

## Tecnologías
- Python 3
- Módulos estándar: `csv`, `os`, `datetime`

## Cómo usarlo
1. Clona el repositorio:
```
git clone https://github.com/AngelPedrazaContreras12/gestor-gastos.git
```
2. Entra a la carpeta y ejecuta:
```
cd gestor-gastos
python gastos.py
```

## Ejemplo
```
=== GESTOR DE GASTOS ===
1. Agregar gasto
2. Ver gastos
3. Resumen por categoria
4. Salir
```