# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    """
    Lee un archivo donde hay UN número por línea y retorna el promedio de
    los números válidos (como float).

    Reglas:
    - Las líneas que no se puedan convertir a float deben ignorarse (usar
      try/except ValueError internamente).
    - Las líneas vacías también se ignoran.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo existe pero no contiene ningún número válido, lanzar
      ValueError("no valid numbers").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        float - promedio de los números válidos.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si no hay números válidos en el archivo.

    Ejemplo:
        # archivo contiene: "10\n20\nno_es_un_numero\n30\n"
        safe_average("numeros.txt") -> 20.0
    """
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("Archivo no encontrado")

    suma = 0
    cont = 0
    with open(filename, "r") as arch:
        for linea in arch:
            try:
                num = float(linea)
                suma += num
                cont += 1
            except ValueError:
                continue
        if cont == 0:
            raise ValueError("no valid numbers")
    prom = suma / cont
    return prom
#print(safe_average("tp-8-exceptions-and-files-sorsini-austral-main\\data\\ej04_numeros.txt"))
#print(safe_average("tp-8-exceptions-and-files-sorsini-austral-main\\data\\ej04_sin_numeros.txt"))