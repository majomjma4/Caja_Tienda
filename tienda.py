# Catálogo 

catalogo = []
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

#Menú

print("""---Bienvenido---
Escoja una opción:
1. Ver catálogo
2. Agregar al carrito
3. Ver carrito
4. finalizar compra
0. Salir
      """)

opcion = int(input("Ingrese la opción: "))

