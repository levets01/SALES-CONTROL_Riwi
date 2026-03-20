from funciones import registroCLientes
from funciones import registroProductos
from funciones import pedido
from funciones import mostrar_ingresos
from funciones import resumen_general
from funciones import ver_ingresos_totales

def menu_principal():
    """
    Menú interactivo para el taller semanal:
    - Registrar clientes
    - Registrar productos
    - Realizar pedidos
    - Mostrar reportes de ingresos
    - Mostrar resumen general
    """

    mis_clientes = None
    mis_productos = None
    datos_pedidos = None

    while True:
        # Banner ASCII al inicio del menú
        print("""
 ██████╗ ███████╗███████╗████████╗██╗ ██████╗ ███╗   ██╗    ██████╗ ███████╗    ██████╗ ███████╗██████╗ ██╗██████╗  ██████╗ ███████╗
██╔════╝ ██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║    ██╔══██╗██╔════╝    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗██╔════╝
██║  ███╗█████╗  ███████╗   ██║   ██║██║   ██║██╔██╗ ██║    ██║  ██║█████╗      ██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║███████╗
██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╗██║    ██║  ██║██╔══╝      ██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║╚════██║
╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚████║    ██████╔╝███████╗    ██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝███████║
 ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝ ╚══════╝    ╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝
""")

        # Menú de opciones
        print("=== MENÚ PRINCIPAL ===")
        print("1. Registrar clientes")
        print("2. Registrar productos")
        print("3. Realizar pedidos")
        print("4. Ver reporte de ingresos")
        print("5. Ver resumen general")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            mis_clientes = registroCLientes()
            print("\nClientes registrados con éxito.")

        elif opcion == "2":
            mis_productos = registroProductos()
            print("\nProductos registrados con éxito.")

        elif opcion == "3":
            if mis_clientes is None or mis_productos is None:
                print("Primero debes registrar clientes y productos.")
                continue
            datos_pedidos = pedido(mis_clientes, mis_productos)
            if datos_pedidos:
                print("\nPedidos realizados con éxito.")
            else:
                print("No se realizaron pedidos.")

        elif opcion == "4":
            if datos_pedidos is None or not datos_pedidos:
                print("No hay pedidos realizados.")
                continue
            reporte_texto, ingreso_total = mostrar_ingresos(datos_pedidos)
            print(reporte_texto)
            totales, suma = ver_ingresos_totales(datos_pedidos)
            print("\nTotales individuales:", totales)
            print("Suma total de ingresos:", suma)

        elif opcion == "5":
            if mis_clientes is None or mis_productos is None or datos_pedidos is None or not datos_pedidos:
                print("Primero debes registrar clientes, productos y pedidos.")
                continue
            resumen = resumen_general(mis_clientes, mis_productos, datos_pedidos)
            print("\n--- REPORTE GENERAL ---")
            print(resumen["reporte_str"])
            print("\nTotales individuales por pedido:", resumen["totales_individuales"])
            print("Suma total de ingresos:", resumen["suma_total"])

        elif opcion == "6":
            print("¡Gracias por usar el sistema! Saliendo...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")



menu_principal()

