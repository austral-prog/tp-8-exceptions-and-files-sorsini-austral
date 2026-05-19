# Ejercicio 3 - Ventas por producto


def read_sales(filename):
    """
    Lee un archivo con ventas en formato "producto:valor;producto:valor;..."
    (todo en una sola línea, los registros separados por ';') y agrupa los
    valores en una lista por producto.

    Reglas:
    - Los valores se convierten a float.
    - El orden de los montos dentro de la lista es el mismo en que aparecen
      en el archivo.
    - Los separadores ';' finales sin contenido se ignoran (es común que
      el archivo termine con ';').
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[float]] - montos de venta agrupados por producto.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "producto1:100;producto2:200;producto1:150;"
        read_sales("ventas.txt") -> {
            "producto1": [100.0, 150.0],
            "producto2": [200.0],
        }
    """
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("Archivo no encontrado")
    
    dicc = {}
    with open(filename,"r") as arch:
        contenido = arch.read()
        valores = contenido.split(";")
        
        for valor in valores:
            valor = valor.strip()
            if valor:
                producto, precio = valor.split(":")
                precio = float(precio)
                
                if producto in dicc:
                    dicc[producto].append(precio)
                else:
                    dicc[producto] = [precio]
    return dicc
#print(read_sales("tp-8-exceptions-and-files-sorsini-austral-main\\data\\ej03_ventas.txt"))

def process_sales(data):
    """
    Para cada producto del diccionario, imprime en el orden natural del dict:

        producto: ventas totales $X.XX, promedio $Y.YY

    Los valores de total y promedio deben mostrarse siempre con DOS
    decimales.

    Args:
        data: dict[str, list[float]] - salida de read_sales.

    Returns:
        None

    Ejemplo:
        process_sales({"producto1": [100.0, 150.0]})
        # imprime: "producto1: ventas totales $250.00, promedio $125.00"
    """
    for producto, valores in data.items():
        suma = 0
        for valor in valores:
            suma += valor
        ventas_totales = suma
        promedio = ventas_totales / len(valores)
        print(f"{producto}: ventas totales ${ventas_totales:.2f}, promedio ${promedio:.2f}")
#process_sales({"producto1": [100.00, 150.00]})