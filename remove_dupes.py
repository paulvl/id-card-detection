import os
import hashlib

def obtener_hash_archivo(ruta_archivo):
    BUF_SIZE = 65536  # Tamaño del búfer para calcular el hash
    sha256 = hashlib.sha256()
    with open(ruta_archivo, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def eliminar_imagenes_duplicadas(carpeta):
    hashes = {}  # Diccionario para almacenar hashes y rutas de archivos duplicados

    # Recorre los archivos en la carpeta
    for foldername, _, filenames in os.walk(carpeta):
        for filename in filenames:
            ruta_archivo = os.path.join(foldername, filename)

            # Ignora los archivos que no son imágenes
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                continue

            # Calcula el hash del archivo
            h = obtener_hash_archivo(ruta_archivo)

            # Si el hash ya está en el diccionario, agrega el archivo a la lista de duplicados
            if h in hashes:
                hashes[h].append(ruta_archivo)
            else:
                # Si no está en el diccionario, agrega el hash y la ruta de archivo
                hashes[h] = [ruta_archivo]

    # Elimina los archivos duplicados manteniendo solo una copia de cada imagen
    for lista_duplicados in hashes.values():
        if len(lista_duplicados) > 1:
            original = lista_duplicados[0]
            duplicados = lista_duplicados[1:]
            for duplicado in duplicados:
                print(f"Eliminando duplicado: {duplicado}")
                os.remove(duplicado)

if __name__ == "__main__":
    carpeta_data = "./data"
    eliminar_imagenes_duplicadas(carpeta_data)
