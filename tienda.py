 
catalogo = []
carrito = []  

def agg_prod (codigo, nombre, precio, stock):
    producto = {
        "codigo": codigo,
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
    print("""---Bienvenido---
Escoja una opción:
1. Ver catálogo
2. Agregar al carrito
3. Ver carrito
4. finalizar compra
0. Salir
""")
    
    opcion = int(input("Ingrese la opción: "))
    
    if opcion == 1:
        
        for prod in catalogo:
            print(f"\n{prod['codigo']} | {prod['nombre']} |  {prod['precio']} | {prod['stock']}")
            
        while True:
            volver = input("\nIngrese 9 para regresar al menú principal: ")
            if volver == "9":
                break
            
        
    elif opcion == 2:
            
        codigo_buscar = input("Agrege el codigo del producto que desea agregar: ").upper()
            
        producto_encontrado = None
            
        for prod in catalogo:
            if prod["codigo"] == codigo_buscar:
                producto_encontrado = prod
                break
            
        if producto_encontrado:
            cantidad = int(input("Ingrese la cantidad: "))
                    
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                
            elif cantidad > producto_encontrado["stock"]:
                print(f"No hay suficiente en stock. Disponible: {producto_encontrado['stock']}")
            else:
                carrito.append({
                    "codigo": producto_encontrado["codigo"],
                    "nombre": producto_encontrado["nombre"],
                    "precio": producto_encontrado["precio"],
                    "cantidad": cantidad
                })
                producto_encontrado["stock"] -= cantidad
                print(f"{cantidad} unidades de {producto_encontrado['nombre']} se agregaron al carrito")
        
        else: 
            print("Producto no encontrado ")  
            
        while True:
            volver = input("\nIngrese 9 para regresar al menú principal: ")
            if volver == "9":
                break   
    
    elif opcion == 3:
        
        if not carrito:
            print("El carrito está vacío")
        
        else: 
            print("\n---Carrito de compras---")
            total=0
            
            for car in carrito:
                subtotal = car["precio"] * car["cantidad"]
                total += subtotal
                print(f"{car['nombre']} - ${car['precio']} x {car['cantidad']} = ${subtotal:.2f}")
            
            print(f"\nTotal: ${total:.2f}")
        
        while True:
            volver = input("\nIngrese 9 para regresar al menú principal: ")
            if volver == "9":
                break
    
    elif opcion == 4:
        
        if not carrito:
            print("El carrito está vacío")
        
        else:
            print("\n========== FACTURA ==========")
            print(f"{'Producto':<15}{'cant.':<6}{'Precio':<10}{'Subtotal':<10}")
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
           
            else:
                print(f"{'No aplica descuento':<30}")
                
            print(f"{'IVA 15%:':<30}${iva:.2f}")
            print(f"{'TOTAL A PAGAR:':<30}${total_final:.2f}")
            print("==============================\n")
            
        while True:
            volver = input("\nIngrese 9 para regresar al menú principal: ")
            if volver == "9":
                break
            
   
            
            