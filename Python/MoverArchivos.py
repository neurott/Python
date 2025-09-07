import shutil
import os

def move_files(origenes, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

    for origen in origenes:  # mira todas las carpetas
        if os.path.exists(origen):  # verifica si la carpeta existe
            for archivo in os.listdir(origen):
                ruta_archivo = os.path.join(origen, archivo)
                if os.path.isfile(ruta_archivo):
                    shutil.move(ruta_archivo, os.path.join(destino, archivo))
            print(f"Archivos de {origen} movidos exitosamente")
        else:
            print(f"La carpeta {origen} no esta, no se que pasó")
    
    archivos = [archivo for archivo in os.listdir(origen) if os.path.isfile(os.path.join(origen, archivo))]
    total_archivos=len(archivos)
      
    if total_archivos == 0:
        print("No hay nada para mover")
        return
# PATH CONFIG
carpeta_origen = [
    r"E:\descargas",
    r"F:\Downloads",
    r"D:\Downloads"
]
carpeta_destino = r"H:\descargas"

move_files(carpeta_origen, carpeta_destino)
