import os
import shutil

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

def mover_archivos_por_prefijo(carpeta):
    prefijos = obtener_prefijos_archivos(carpeta)

    # Crea una carpeta por cada prefijo
    for prefijo in prefijos:
        nueva_carpeta = os.path.join(carpeta, prefijo)
        os.makedirs(nueva_carpeta, exist_ok=True)

    # Mueve los archivos a sus respectivas carpetas
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
            nueva_carpeta = os.path.join(carpeta, prefijo)
            nueva_ruta_archivo = os.path.join(nueva_carpeta, filename)
            shutil.move(ruta_archivo, nueva_ruta_archivo)
        else:
            # Si no hay guion bajo, mueve el archivo a la carpeta raíz
            nueva_ruta_archivo = os.path.join(carpeta, filename)
            shutil.move(ruta_archivo, nueva_ruta_archivo)

if __name__ == "__main__":
    carpeta_data = "./data"
    mover_archivos_por_prefijo(carpeta_data)
