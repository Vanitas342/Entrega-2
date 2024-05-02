import cv2
import os
import random

# Directorio de entrada de las imágenes
input_images_patch = "C:/Users/nicoc/OneDrive/Documentos/Entrega 2/Imagenes Entrega 2"

# Obtener la lista de carpetas en el directorio
folders_names = os.listdir(input_images_patch)
print(folders_names)

# Resolución deseada
new_width = 800
new_height = 600

for folder_name in folders_names:
    # Ruta completa de la carpeta de imágenes
    folder_path = os.path.join(input_images_patch, folder_name)
    
    # Obtener la lista de nombres de archivos en la carpeta
    files_names = os.listdir(folder_path)
    
    # Verificar si hay imágenes en la carpeta
    if len(files_names) > 0:
        # Elegir una imagen aleatoria de la carpeta
        image_name = random.choice(files_names)
        image_path = os.path.join(folder_path, image_name)
        
        # Leer la imagen
        image = cv2.imread(image_path)

        # Cambiar la resolución de la imagen
        resized_image = cv2.resize(image, (new_width, new_height))

        # Mostrar la imagen
        cv2.imshow("Resized Image", resized_image)
        cv2.waitKey(0)
    else:
        print(f"No se encontraron imágenes en la carpeta: {folder_path}")

cv2.destroyAllWindows()