import os
import img2pdf

imagenes_jpg = [archivo for archivo in os.listdir(
    './') if archivo.endswith(".jpeg")]

with open("Conversion.pdf", "wb") as documento:
    documento.write(img2pdf.convert(imagenes_jpg))
