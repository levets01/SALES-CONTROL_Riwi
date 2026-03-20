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
    
    opcion = menu_principal()
    while True: 
           
                   
            
        if opcion == "1":
            print("=== REGISTRAR CLIENTE ===")
            registroCLientes()
            print("Cliente registrado ✔")
            pausar()
            continue

        elif opcion == "2":
            print("=== REGISTRAR PRODUCTO ===")
            registroProductos()
            continue

            
            print("Producto registrado ✔")
            pausar()
            continue
        
        elif opcion == "3":
            print("=== CREAR PEDIDO ===")
            pedido()
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
