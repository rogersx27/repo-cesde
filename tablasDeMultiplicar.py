import random
import pandas as pd


def cantidad_ventas(lista_productos):
    contador_mayores = sum(
        1 for producto in lista_productos if producto["precio"] >= 200000
    )
    contador_menores = sum(
        1 for producto in lista_productos if producto["precio"] < 200000
    )

    return contador_mayores, contador_menores


def filtro_ventas(lista_productos):
    total_ventas_mayores = sum(
        productos["precio"]
        for productos in lista_productos
        if productos["precio"] >= 200000
    )

    total_ventas_menores = sum(
        productos["precio"]
        for productos in lista_productos
        if productos["precio"] < 200000
    )

    return total_ventas_mayores, total_ventas_menores


def total_ventas(lista_productos):
    return sum(producto["precio"] for producto in lista_productos)


def crear_producto():

    nombres_productos = [
        "Camiseta",
        "Pantalón",
        "Zapatos",
        "Sombrero",
        "Bufanda",
        "Gorra",
        "Reloj",
        "Bolso",
        "Gafas",
        "Chaqueta",
    ]

    producto = random.choice(nombres_productos)
    cantidad = random.randint(1, 100)
    precio = random.randint(10000, 1000000)
    subtotal = cantidad * precio

    producto_dict = {
        "nombre_producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "subtotal": subtotal,
    }

    return producto_dict


if __name__ == "__main__":
    lista_productos = []

    for i in range(100):
        producto = crear_producto()
        lista_productos.append(producto)

    print("Productos creados con éxito.")

    df = pd.DataFrame(lista_productos)
    print(df)

    totalVentas = total_ventas(lista_productos)
    filtroVentas = filtro_ventas(lista_productos)
    cantidadVentas = cantidad_ventas(lista_productos)

    print(
        f"""
    Cantidad de ventas totales = {sum(cantidadVentas)}

    Total de ventas >= 200000 = {filtroVentas[0]}
    Cantidad de ventas = {cantidadVentas[0]}

    Total de ventas < 200000 = {filtroVentas[1]}
    Cantidad de ventas = {cantidadVentas[1]}

    Subtotal de ventas = {totalVentas}
    """
    )
