# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    """
    Lee el archivo, lo divide en palabras (separadas por cualquier tipo
    de whitespace) y retorna la palabra más larga.

    Reglas:
    - Si hay varias palabras con la misma longitud máxima, retornar la
      PRIMERA en aparecer.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo no tiene ninguna palabra (está vacío o solo tiene
      espacios/saltos de línea), lanzar ValueError("file has no words").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        str - la palabra más larga del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si el archivo no tiene palabras.

    Ejemplo:
        # archivo contiene: "el gato corre rapido\npor el jardin\n"
        find_longest_word("texto.txt") -> "rapido"
    """
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("Archivo no encontrado")

    with open(filename, "r") as arch:
        contenido = arch.read().split()
        if not contenido:
            raise ValueError("file has no words")
        else:
            max = contenido[0]
            for palabra in contenido:
                if len(palabra) > len(max):
                    max = palabra
    return max
#print(find_longest_word("tp-8-exceptions-and-files-sorsini-austral-main\\data\\ej08_texto.txt"))