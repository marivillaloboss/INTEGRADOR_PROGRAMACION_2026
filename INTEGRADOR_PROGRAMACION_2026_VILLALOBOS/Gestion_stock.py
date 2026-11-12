stock_productos = {"enlatados": [],"bebidas": [],"lacteos": []}
stock_cantidades = {"enlatados": [],"bebidas": [],"lacteos": []}
def inicializar():
    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []
def cargar_stock():
    categoria = input("Ingrese la categoria del producto (enlatados, bebidas, lacteos): ")
    if categoria in stock_productos:
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        stock_productos[categoria].append(producto)
        stock_cantidades[categoria].append(cantidad)
    else:
        print("Categoria no valida.")
def mostrar_stock():
    for categoria in stock_productos:
        print("Categoria:", categoria)
        for i in range(len(stock_productos[categoria])):
            print("Producto:", stock_productos[categoria][i], "Cantidad:", stock_cantidades[categoria][i])
def contar(lista_productos):
    print("La cantidad de productos en la lista es:", len(lista_productos))
    total = 0
    for cantidad in lista_productos:
        total = total + cantidad
    print("El total de productos en la lista es:", total)