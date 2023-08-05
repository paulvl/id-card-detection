import os

def obtener_extensiones_carpeta(carpeta):
    extensiones = set()

    # Recorre los archivos en la carpeta
    for filename in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, filename)

        # Verifica si el elemento es un archivo
        if os.path.isfile(ruta_archivo):
            # Obtiene la extensión del archivo
            extension = os.path.splitext(filename)[1].lower()
            extensiones.add(extension)

    return extensiones

if __name__ == "__main__":
    carpeta_data = "./data"
    extensiones_encontradas = obtener_extensiones_carpeta(carpeta_data)

    print("Extensiones encontradas en la carpeta:")
    for extension in extensiones_encontradas:
        print(extension)