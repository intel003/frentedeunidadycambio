import shutil
import subprocess
import sys
import os

def main():
    workspace = 'c:/Users/sebas/Documents/agrupacioncelesteverde'
    os.makedirs(workspace, exist_ok=True)

    print("Copiando fondo...")
    # Copy fondo
    shutil.copy(
        'C:/Users/sebas/.gemini/antigravity/brain/e4b8cbea-7c5a-46fb-8731-8d2dd5ff6cf8/.user_uploaded/media_1788565898141.jpg', 
        os.path.join(workspace, 'fondo.jpg')
    )
    
    print("Instalando dependencias para procesar imagen...")
    try:
        import rembg
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rembg", "Pillow", "onnxruntime"])
        import rembg
    
    from PIL import Image
    
    input_path = 'C:/Users/sebas/.gemini/antigravity/brain/e4b8cbea-7c5a-46fb-8731-8d2dd5ff6cf8/.user_uploaded/media_1788565912277.jpg'
    output_path = os.path.join(workspace, 'referentes.png')
    
    print("Procesando imagen de las referentes...")
    img = Image.open(input_path)
    
    # Recortar la imagen antes de quitar el fondo para eliminar los textos.
    # Recortamos aprox el 12% superior y el 20% inferior basado en la imagen proporcionada.
    width, height = img.size
    img_cropped = img.crop((0, int(height * 0.12), width, int(height * 0.81)))
    
    print("Removiendo fondo...")
    output = rembg.remove(img_cropped)
    
    print("Guardando imagen resultante...")
    output.save(output_path)
    print("Proceso finalizado exitosamente.")

if __name__ == '__main__':
    main()
