# TFG-TreeTopDetector
Cree un ambiente virtual que utilice python 3.7
    Anaconda Navigator 2.1.1 es el utilizado

El video https://www.youtube.com/watch?v=Fu_km7FXyaU muestra lo basico para configurar el modelo de MASK-RCNN tanto para entrenamiento como inferencias(predicciones)

Se necesita descargar la bilbioteca Mask-RCNN e incluir la carpeta completa en el directorio de este proyecto.
    https://github.com/ahmedfgad/Mask-RCNN-TF2

Para Entrenamiento
    La carpets tree-detection debe ser incluinda dentro de la carpeta del repositorio clonado de Mask-RCNN
    Debe incluir dentro de la carpeta tree-detection los pesos del modelo pre entrenado de Mask
        https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5
    El archivo treetop_maskrcnn_coco_style_labels.py es donde se realiza el entrenamiento

Para Inferencias

Reemplace el archivo requirements.txt del la bilbioteca clonada por el que se encuentra en este proyecto, ya que incluye todas las versiones de las bibliotecas correspondientes. Instale de accuerdo con las instrucciones del repositorio original. Para instalacion y configuracion puede apoyarse con el siguiente video:
    https://www.youtube.com/watch?v=Fu_km7FXyaU


Para crear el ejecutable:

    pyinstaller --name=myapp3 --add-data "C:\Users\MyPathAlModeloEntrenado\MyModelE.h5;." GUI.py

Se crean 2 carpetas automaticamente al finalizar la ejecucion de Pyinstaller,
    dist
    build

dist es la que contiene el archivo ejecutable. Copie toda la carpeta y sus archivos donde necesite, cree un acceso directo al ejecutable, en este caso myapp3.exe

Y eso es todo

Cualquier duda, puede contactarme al correo: vic.arhz@gmail.com

