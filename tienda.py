 
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