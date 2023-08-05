import os
import shutil
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk

def resize_proporcional_con_alto_maximo(imagen, alto_maximo):
    ancho_original, alto_original = imagen.size
    proporcion = alto_maximo / float(alto_original)
    nuevo_ancho = int(ancho_original * proporcion)
    nuevo_alto = alto_maximo
    imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
    return imagen_redimensionada

def obtener_rutas_imagenes(carpeta):
    imagenes = []
    for filename in os.listdir(carpeta):
        ruta_imagen = os.path.join(carpeta, filename)
        if os.path.isfile(ruta_imagen) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            imagenes.append(ruta_imagen)
    return imagenes

def mostrar_siguiente_imagen():
    global indice_actual
    global archivo_imagen
    if indice_actual < len(rutas_imagenes):
        archivo_imagen = rutas_imagenes[indice_actual]
        img = Image.open(archivo_imagen)
        img = resize_proporcional_con_alto_maximo(img, 1000)
        img_tk = ImageTk.PhotoImage(img)
        imagen_label.config(image=img_tk)
        imagen_label.image = img_tk
        indice_actual += 1
    else:
        imagen_label.config(image=None)
        imagen_label.image = None
        print("No hay más imágenes para mostrar.")
        ventana.quit()

def mover_imagen_valida():
    print("moviendo imagen valida")
    print(archivo_imagen)
    if archivo_imagen:
        shutil.move(archivo_imagen, os.path.join(carpeta_valid, os.path.basename(archivo_imagen)))
        mostrar_siguiente_imagen()

def mover_imagen_invalida():
    print("moviendo imagen invalida")
    print(archivo_imagen)
    if archivo_imagen:
        shutil.move(archivo_imagen, os.path.join(carpeta_invalid, os.path.basename(archivo_imagen)))
        mostrar_siguiente_imagen()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Clasificador de Imágenes")
ventana.geometry("1900x1200")

# Carpeta destino para las imágenes válidas e inválidas
carpeta_data = "./data/front"
carpeta_valid = "./data/front/valid"
carpeta_invalid = "./data/front/invalid"
os.makedirs(carpeta_valid, exist_ok=True)
os.makedirs(carpeta_invalid, exist_ok=True)

# Obtener las rutas de las imágenes en la carpeta
rutas_imagenes = obtener_rutas_imagenes(carpeta_data)
indice_actual = 0

# Etiqueta para mostrar la imagen
imagen_label = tk.Label(ventana)
imagen_label.pack(pady=10)

# Botones
boton_valida = tk.Button(ventana, text="Válida", command=mover_imagen_valida)
boton_invalida = tk.Button(ventana, text="Inválida", command=mover_imagen_invalida)
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)

boton_valida.pack(side=tk.LEFT, padx=10)
boton_invalida.pack(side=tk.LEFT, padx=10)
boton_salir.pack(side=tk.RIGHT, padx=10)

archivo_imagen = None
mostrar_siguiente_imagen()

ventana.mainloop()
