# Sistema de Gestión de Productos

productos = []


def cargar_datos():
    """Cargar los productos desde el archivo productos.txt al iniciar el programa."""
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(", ")
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
    except FileNotFoundError:
        print("Archivo de productos no encontrado. Se iniciará una lista vacía.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")


def guardar_datos():
    """Guardar los productos en el archivo productos.txt."""
    try:
        with open("productos.txt", "w") as archivo:
            for producto in productos:
                archivo.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al guardar los datos: {e}")


def añadir_producto():
    """Añadir un nuevo producto a la lista."""
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Precio o cantidad inválidos. Inténtalo de nuevo.")
    
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
    print(f"Producto '{nombre}' añadido correctamente.")


def ver_productos():
    """Mostrar todos los productos de la lista."""
    if productos:
        print("\nLista de productos:")
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")
    else:
        print("\nNo hay productos en la lista.")


def actualizar_producto():
    """Actualizar los detalles de un producto existente."""
    ver_productos()
    if productos:
        try:
            indice = int(input("Selecciona el número del producto a actualizar: ")) - 1
            if 0 <= indice < len(productos):
                producto = productos[indice]
                print(f"Producto seleccionado: {producto['nombre']}")
                nuevo_nombre = input(f"Nuevo nombre (deja en blanco para mantener '{producto['nombre']}'): ")
                nuevo_precio = input(f"Nuevo precio (deja en blanco para mantener {producto['precio']}): ")
                nueva_cantidad = input(f"Nueva cantidad (deja en blanco para mantener {producto['cantidad']}): ")

                if nuevo_nombre:
                    producto['nombre'] = nuevo_nombre
                if nuevo_precio:
                    producto['precio'] = float(nuevo_precio)
                if nueva_cantidad:
                    producto['cantidad'] = int(nueva_cantidad)

                print(f"Producto '{producto['nombre']}' actualizado correctamente.")
            else:
                print("Producto no encontrado.")
        except ValueError:
            print("Entrada inválida.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar el producto: {e}")


def eliminar_producto():
    """Eliminar un producto basado en su nombre."""
    ver_productos()
    if productos:
        try:
            indice = int(input("Selecciona el número del producto a eliminar: ")) - 1
            if 0 <= indice < len(productos):
                producto_eliminado = productos.pop(indice)
                print(f"Producto '{producto_eliminado['nombre']}' eliminado correctamente.")
            else:
                print("Producto no encontrado.")
        except ValueError:
            print("Entrada inválida.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el producto: {e}")


def menu():
    """Mostrar el menú principal del sistema."""
    cargar_datos()  # Cargar los datos al iniciar el programa
    while True:
        print("\n---- Sistema de Gestión de Productos ----")
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


# Ejecutar el menú del sistema
if __name__ == "__main__":
    menu()
