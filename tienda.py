 
catalogo = []
carrito = []  

def agg_prod (codigo, nombre, precio, stock):
    producto = {
        "codigo": codigo.strip().upper(),
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    catalogo.append(producto)

agg_prod("P001", "Azucar", 2.50, 100)
agg_prod("P002", "Sal", 1.00, 100)
agg_prod("P003", "Atún", 1.65, 100)
agg_prod("P004", "Fideos", 0.75, 100)
agg_prod("P005", "Cola", 1.00, 100)
agg_prod("P006", "Jugo", 0.50, 100)


while True:
    print("""
\nEscoja una opción:
1. Ver catálogo
2. Agregar al carrito
3. Ver carrito
4. finalizar compra
0. Salir
\n""")
    
    try:
        opcion = int(input("\nIngrese la opción: "))
        
    except ValueError:
        print("Ingrese un número válido")
        continue
    
    match opcion:
        case 1:
            
            print("\n---Catálogo---")
            for prod in catalogo:
                print(f"\n{prod['codigo']} | {prod['nombre']} |  {prod['precio']} | {prod['stock']}\n")
            
          
        case 2:
            
            codigo_buscar = input("\nAgrege el codigo del producto que desea agregar: ").strip().upper()
                
            producto_encontrado = None
            
            for prod in catalogo:
                if prod["codigo"] == codigo_buscar:
                    producto_encontrado = prod
                    break
                
            if producto_encontrado:
                try:
                    
                    cantidad = int(input("\nIngrese la cantidad: "))
                except ValueError:
                    print("\nCantidad inválida")
                    continue
                    
                if cantidad <= 0:
                    print("\nLa cantidad debe ser mayor a 0")
                    
                elif cantidad > producto_encontrado["stock"]:
                    print(f"\nNo hay suficiente en stock. Disponible: {producto_encontrado['stock']}")
                else:
                    carrito.append({
                        "codigo": producto_encontrado["codigo"],
                        "nombre": producto_encontrado["nombre"],
                        "precio": producto_encontrado["precio"],
                        "cantidad": cantidad
                    })
                    producto_encontrado["stock"] -= cantidad
                    print(f"{cantidad} unidades de {producto_encontrado['nombre']} se agregaron al carrito\n")
            
            else: 
                print("\nProducto no encontrado ")  
 
    
        case 3:
        
            if not carrito:
                print("\nEl carrito está vacío")
            
            else: 
                print("\n---Carrito de compras---")
                total=0
                
                for car in carrito:
                    subtotal = car["precio"] * car["cantidad"]
                    total += subtotal
                    print(f"{car['nombre']} - ${car['precio']} x {car['cantidad']} = ${subtotal:.2f}\n")
                
                print(f"\nTotal: ${total:.2f}")
            
        case 4:
            if not carrito:
                print("\nEl carrito está vacío")
                continue
        
            compra= input("\nDesea finalizar la compra (si/no): ")
            if compra == 'si':

                print("\n================== FACTURA ==================")
                print(f"{'Producto':<15}{'cant.':<6}{'Precio':<10}{'Subtotal':<10}\n")
                print("-"*45)
                
                total = 0
                
                for car in carrito:
                    subtotal = car["precio"] * car["cantidad"]
                    total += subtotal
                    print(f"{car['nombre']:<15}{car['cantidad']:<6}{car['precio']:<9.2f}${subtotal:<9.2f}")
                    
                if total > 50:
                    descuento = 0.10
                elif total > 20:
                    descuento = 0.05
                else:
                    descuento = 0
                    
                total_con_descuento = total * (1-descuento)
                iva = total_con_descuento * 0.15
                total_final = total_con_descuento + iva
                
                print("-"*45)
                print(f"{'Total sin descuento: ':<30}${total:.2f}")
                if descuento > 0:
                    print(f"{'Descuento aplicado: ':<30}{int(descuento*100)}%")
                    print(f"{'Total con descuento: ':<30}${total_con_descuento:.2f}")   
                print(f"{'IVA 15%:':<30}${iva:.2f}")
                print(f"{'TOTAL A PAGAR:':<30}${total_final:.2f}")
                print("===============================================\n")
         
            else:
                print("compra cancelada")
               
        case 0:    
                
            print("\n ¡Gracias por su compra! Hasta luego. \n ")   
            carrito.clear()
                
            continue
                
        case _:
            print("¡Error, Opción inválida    \n") 
                
                       
            