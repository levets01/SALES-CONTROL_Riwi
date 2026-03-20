from funciones import registroCLientes
from funciones import registroProductos
from funciones import pedido
from funciones import mostrar_ingresos
from funciones import resumen_general
from funciones import ver_ingresos_totales
from funciones import limpiar_pantalla
from funciones import pausar
import os 

from menu import menu_principal

def main():
    mis_clientes = {}
    mis_productos = {}
    pedidos = {}

    while True: 
        #limpiar_pantalla()
        print(menu_principal())

        opcion = menu_principal()

        if opcion == "1":
            print("=== REGISTRAR CLIENTE ===")
            registroCLientes()
            #clientes = registroCLientes(clientes, cid, nombre, correo)
            print("Cliente registrado ✔")
            pausar()
            continue

        elif opcion == "2":
            print("=== REGISTRAR PRODUCTO ===")
            registroProductos()
            

            #productos = registroProductos(productos, pid, nombre, precio)
            print("Producto registrado ✔")
            pausar()
            continue
        
        elif opcion == "3":
            print("=== CREAR PEDIDO ===")
            pedido()

        
            #pedidos = pedido(pedidos, pedido_id, cliente, producto, cantidad, precio)
            print("Pedido creado ✔")
            pausar()
            continue

        elif opcion == "4":
            mostrar_ingresos()
            pausar()
            continue

        elif opcion == "5":
            ingresos = ver_ingresos_totales(pedidos)
            print(f"\nTotal ingresos: {ingresos}")
            pausar()
            continue

        elif opcion == "6":
            print(resumen_general(pedidos))
            pausar()
            continue

        elif opcion == "7":
            print("Saliendo...")
            break
        

        else:
            print("Opción inválida")
            pausar()





main()
