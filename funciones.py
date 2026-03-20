import os 
## THIS FUCTION 

def limpiar_pantalla():
    os.system("cls"if os.name == "nt" else "clear")
    return""

def pausar():
    input("Precione ENTER para continuar....")           
    return""


def registroCLientes ():
    #diccionari vacio donde se guardan clientes
    clientes = {}

    x = int(input("digite el numero de clientes: "))

    for i in range(x):
        while True:
            try:
                id_cliente = int(input(f"digite el id del cliente {i+1}: "))
                if id_cliente > 0:
                    clientes[id_cliente]= {
                "nombre": input("escribe el nombre :" ),
                "correo" : input("escribe el correo: ")
                     
                }  
                    break
        

                else:
                    print("el id debe ser un numero positivo.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
        
    return clientes
                           
                           
## 

contador_pedidos = 1

def registroProductos ():
  
    global contador_pedidos 
    productos = {}

    x = int(input("digite el numero de productos a registrar : "))

    for i in range(x):
        while True:
            try:
                id_producto = int(input(f"digite el id del producto {i+1}: "))
                if id_producto > 0:
                    productos[id_producto]= {
                "nombre_producto": input("escribe el nombre: "),
                "precio" : int(input("escribe el precio: ")),
                "stock": int(input("escribe la cantidad en inventario: ")) 
                }  
                    break
        

                else:
                    print("el id del producto debe ser mayor a 0.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
        
    return productos
                      
                      
###

def pedido (db_clientes, db_productos):

  pedidos = () ##tupla vacia 
  while True:
    try:
        cant_pedido = int(input("cuantos pedidos desea realizar: "))

        if cant_pedido <= 0:
            print("La cantidad debe de ser un valor positivo")
        else:
            break

    except ValueError:
            print("Debe ingresar un número válido.")
            

  for i in range(cant_pedido):
    print(f"pedido {i+1}")

    try:

        id_c = int(input("Ingrese el ID del cliente que compra: "))
        id_p = int(input("Ingrese el ID del producto: "))
        

        if id_c in db_clientes and id_p in db_productos:

             while True:
                    try:
                        cant_producto = int(input("Ingrese la cantidad de producto: "))
                        stock_disponible = db_productos[id_p]["stock"]

                        if cant_producto <= 0:
                            print("La cantidad debe ser mayor a 0.")
                        elif cant_producto > stock_disponible:
                            print(f"Stock insuficiente. Disponible: {stock_disponible}")
                        else:
                            break  

                    except ValueError:
                        print("Debe ingresar un número válido.")


             cliente = db_clientes [id_c]["nombre"]
             producto = db_productos[id_p] ["nombre_producto"]
             precio = db_productos[id_p] ["precio"]

             total = cant_producto * precio

             db_productos[id_p]["stock"] -= cant_producto
            ##creamos tupla
            # guardamos clientes productos cantidades y total

            #creamos una tupla para el pedido

             pedido_actual = (id_c, cliente, producto, cant_producto, precio, total)

             pedidos = pedidos + (pedido_actual,)

            
        else:
            return "Error: Cliente o Producto no encontrado en la base de datos."
            
    except ValueError:
        print( "Error: Los IDs y la cantidad deben ser números enteros.")

  return pedidos    


####



def mostrar_ingresos(pedidos):
    total_general = 0
    reporte = "\n===== REPORTE DE INGRESOS =====\n"

    for i, p in enumerate(pedidos, start=1):
        id_c, cliente, producto, precio, cantidad, total = p

        reporte += f"\nPedido {i}:\n"
        reporte += f"Cliente: {cliente} (ID: {id_c})\n"
        reporte += f"Producto: {producto}\n"
        reporte += f"Precio unitario: {precio}\n"
        reporte += f"Cantidad: {cantidad}\n"
        reporte += f"Total: {total}\n"

        total_general += total

    reporte += "\n===============================\n"
    reporte += f"Ingreso total generado: {total_general}"

    return reporte, total_general


def ver_ingresos_totales(pedidos):
    totales = ()
    suma = 0

    for p in pedidos:  
        total = p[5]
        totales = totales + (total,)
        suma += total

    return totales, suma
    

def resumen_general(clientes, productos, pedidos):
    
    totales_individuales = ()
    total_general = 0
    reporte = "\n REPORTE GENERAL DE INGRESOS\n"

    # Información de clientes
    reporte += f"\nNúmero de clientes registrados: {len(clientes)}\n"
    reporte += "Clientes:\n"
    for id_c, datos in clientes.items():
        reporte += f"  ID: {id_c}, Nombre: {datos['nombre']}, Correo: {datos['correo']}\n"

    # Información de productos
    reporte += f"\nNúmero de productos registrados: {len(productos)}\n"
    reporte += "Productos:\n"
    for id_p, datos in productos.items():
        reporte += f"  ID: {id_p}, Nombre: {datos['nombre_producto']}, Precio: {datos['precio']}, Stock: {datos.get('stock', 'N/A')}\n"

    # Detalle de pedidos
    for i, p in enumerate(pedidos, start=1):
        id_c, cliente, producto, precio, cantidad, total = p
        reporte += f"\nPedido {i}:\n"
        reporte += f"  Cliente: {cliente} (ID: {id_c})\n"
        reporte += f"  Producto: {producto}\n"
        reporte += f"  Precio unitario: {precio}\n"
        reporte += f"  Cantidad: {cantidad}\n"
        reporte += f"  Total: {total}\n"

        totales_individuales = totales_individuales + (total,)
        total_general += total

    reporte += "\n===============================\n"
    reporte += f"Ingreso total generado: {total_general}\n"

    return {
        "clientes": clientes,
        "productos": productos,
        "pedidos": pedidos,
        "reporte_str": reporte,
        "totales_individuales": totales_individuales,
        "suma_total": total_general
    }

