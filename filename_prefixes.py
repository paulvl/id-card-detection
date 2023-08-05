import os

def obtener_prefijos_archivos(carpeta):
    prefijos = set()

    # Recorre los archivos en la carpeta
    for filename in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, filename)

        # Ignora los elementos que no son archivos
        if not os.path.isfile(ruta_archivo):
            continue

        # Divide el nombre del archivo en el primer guion bajo "_"
        partes = filename.split("_", 1)
        
        # Si el nombre del archivo contiene al menos un guion bajo
        if len(partes) > 1:
            prefijo = partes[0]
            prefijos.add(prefijo)
        else:
            # Si no hay guion bajo, el nombre completo es el prefijo
            prefijos.add(filename)

    return prefijos

if __name__ == "__main__":
    carpeta_data = "./data"
    prefijos_encontrados = obtener_prefijos_archivos(carpeta_data)

    print("Prefijos encontrados en la carpeta:")
    for prefijo in prefijos_encontrados:
        print(prefijo)