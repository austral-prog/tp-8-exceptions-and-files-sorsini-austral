# Ejercicio 1 - Leer líneas de un archivo


def read_lines(filename):
    """
    Lee un archivo de texto y retorna una lista con sus líneas.

    Reglas:
    - Cada línea debe venir sin el salto de línea final y sin espacios
      al principio o al final (strip).
    - Las líneas vacías (o con solo espacios) se ignoran.
    - Si el archivo no existe, se debe propagar FileNotFoundError.
    - Si el archivo está vacío, retornar [].

    Args:
        filename: str - nombre (o ruta) del archivo a leer.

    Returns:
        list[str] - lista de líneas no vacías, en el orden del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "manzana\n  banana\npera\n"
        read_lines("datos.txt") -> ["manzana", "banana", "pera"]
    """
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("Archivo no encontrado")
    
    lista = []
    with open(filename, "r") as arch:
        for linea in arch:
            linea = linea.strip()
            if linea != "": 
                lista.append(linea)
    return lista
#print(read_lines("tp-8-exceptions-and-files-sorsini-austral-main\\data\\ej01_frutas.txt"))