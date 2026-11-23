# Problema 3 - Control de inventario

def calcular_cantidad(stock, minimo):

    if stock < minimo:
        cantidad = minimo - stock
    else:
        cantidad = 0

    return cantidad


def mostrar_inventario():

    inventario = [
        ["P001", "Gaseosa", 8, 20],
        ["P002", "Galletas", 30, 15],
        ["P003", "Chocolate", 4, 12],
        ["P004", "Harina", 10, 25],
        ["P005", "Sal", 18, 10]
    ]

    total = 0

    print("\nCONTROL DE INVENTARIO")
    print("---------------------------------------")

    for producto in inventario:

        codigo = producto[0]
        nombre = producto[1]
        stock = producto[2]
        minimo = producto[3]

        pedir = calcular_cantidad(stock, minimo)

        total = total + pedir

        print(codigo, nombre, "Cantidad a pedir:", pedir)

    print("---------------------------------------")
    print("Total de unidades a pedir:", total)


mostrar_inventario()
