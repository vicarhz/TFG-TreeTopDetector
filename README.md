# TFG-TreeTopDetector
Cree un ambiente virtual que utilice python 3.7

Se necesita descargar la bilbioteca Mask-RCNN e incluir la carpeta completa en el directorio de este proyecto.
    https://github.com/ahmedfgad/Mask-RCNN-TF2

Reemplace el archivo requirements.txt del la bilbioteca clonada por el que se encuentra en este proyecto, ya que incluye todas las versiones de las bibliotecas correspondientes. Instale de accuerdo con las instrucciones del repositorio original. Para instalacion y configuracion puede apoyarse con el siguiente video:
    https://www.youtube.com/watch?v=Fu_km7FXyaU


Para crear el ejecutable:

    pyinstaller --name=myapp3 --add-data "C:\Users\MyPathAlModeloEntrenado\MyModelE.h5;." GUI.py

Se crean 2 carpetas automaticamente al finalizar la ejecucion de Pyinstaller,
    dist
    build

dist es la que contiene el archivo ejecutable. Copie toda la carpeta y sus archivos donde necesite, cree un acceso directo al ejecutable, en este caso myapp3.exe

Y eso es todo

