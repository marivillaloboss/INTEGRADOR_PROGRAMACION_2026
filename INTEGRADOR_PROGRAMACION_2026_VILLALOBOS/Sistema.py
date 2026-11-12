import Menu
import Gestion_stock
def main():
    Gestion_stock.inicializar()
    while True:
        opcion = Menu.mostrar_menu()
        if opcion == 1:
            Gestion_stock.cargar_stock()
        elif opcion == 2:
            Gestion_stock.mostrar_stock()
        elif opcion == 3:
            categoria = input("Ingrese la categoria del producto: ")
            if categoria in Gestion_stock.stock_cantidades:
                Gestion_stock.contar(Gestion_stock.stock_cantidades[categoria])
            else:
                print("Categoria no valida.")
        elif opcion == 4:
            break
        else:
            print("Opcion no valida.")
if __name__ == "__main__":
    main()