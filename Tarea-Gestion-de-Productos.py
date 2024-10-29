productos = []

def añadir_producto():
    # Lógica para añadir un producto
    print("Añadir nombre del producto:")
    nombre=input()
    while True:
        print("Añadir el precio del producto:")
        try:
            precio=float(input())
            break
        except ValueError:
            print("Favor introduzca un precio valido")
    
    while True:
        print("Añadir la cantidad del producto:")
        try:
            cantidad=int(input())
            break
        except ValueError:
            print("Favor introduzca una cantidad valida")
            
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)

def ver_productos():
    # Lógica para ver todos los productos
    if productos == []:
        print("No hay productos")
        return
    
    else:
        print("---------Lista de productos---------")
        for producto in productos:
            print(f"Nombre: {producto ['nombre']}, Precio: {producto ['precio']}, Cantidad: {producto ['cantidad']}")

def actualizar_producto():
    # Lógica para actualizar un producto
    print("Introduce el nombre del producto a actualizar: ")
    nombre = input()
    for producto in productos:
        if producto['nombre'].lower()==nombre.lower():
            while True:
                try:
                    print("Introduce el nuevo precio del producto: ")
                    precio = float(input())
                    break
                except ValueError:
                    print("Favor introduzca el precio nuevo")
                    
            while True:
                try:
                    print("Introduce la cantidad disponible: ")
                    cantidad=int(input())
                    break
                except ValueError:
                    print("Favor introduzca una cantidad valida")
            
            producto['precio']=precio
            producto['cantidad']=cantidad
            print(f"Producto '{nombre}' actualizado correctamente")
            return
    print(f"Producto '{nombre}' no encontrado")

def eliminar_producto():
    # Lógica para eliminar un producto
    print("Introduzca el nombre del producto a eliminar: ")
    nombre=input()
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            return  
    
    print(f'Producto de nombre {nombre} no encontrado')
        
    return productos
        
def guardar_datos():
    # Lógica para guardar los datos en un archivo
    with open('productos.txt','w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    try:
        with open('productos.txt','r') as file:
            read_file = open('productos.txt','r')
            print(read_file.read())
            for line in file:
                nombre, precio, cantidad = line.strip().split(",")
                producto = {"nombre":nombre, "precio": float(precio), "cantidad":int(cantidad)}
                productos.append(producto)
    except FileNotFoundError:
        print("No se encontro el archivo")
            

def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
            
menu()