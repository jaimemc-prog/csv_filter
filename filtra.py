import csv
import os

# ruta de la carpeta que contiene las imágenes
ruta_carpeta_imagenes = './ruta/'

# obtener la lista de nombres de archivo de la carpeta de imágenes
nombres_archivos = os.listdir(ruta_carpeta_imagenes)

# abrir el archivo CSV y leer la columna "image"
with open('./nomArch.csv', 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    nombres_columnas = lector_csv.fieldnames  # obtener los nombres de las columnas
    filas_csv = [fila for fila in lector_csv]

# obtener la lista de nombres de archivo de la columna "image" del archivo CSV
nombres_imagenes_csv = [fila['image'] for fila in filas_csv]

# encontrar las imágenes que no coinciden con los nombres en la columna "image"
imagenes_a_eliminar = [imagen for imagen in nombres_archivos if imagen not in nombres_imagenes_csv]

# eliminar las imágenes que no coinciden con los nombres en la columna "image"
for imagen in imagenes_a_eliminar:
    ruta_imagen = os.path.join(ruta_carpeta_imagenes, imagen)
    os.remove(ruta_imagen)
