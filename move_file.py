import os
import shutil

# Ruta de la carpeta "data"
carpeta_data = "./data"

# Recorre todos los elementos dentro de "data"
for item in os.listdir(carpeta_data):
    # Construye la ruta completa del elemento
    ruta_item = os.path.join(carpeta_data, item)
    
    # Verifica si el elemento es una carpeta
    if os.path.isdir(ruta_item):
        # Recorre los elementos dentro de la subcarpeta
        for sub_item in os.listdir(ruta_item):
            # Construye la ruta completa del sub-elemento
            ruta_sub_item = os.path.join(ruta_item, sub_item)
            
            # Mueve el sub-elemento a la carpeta "data"
            shutil.move(ruta_sub_item, carpeta_data)
        
        # Una vez que los sub-elementos se han movido, elimina la carpeta vacía
        os.rmdir(ruta_item)