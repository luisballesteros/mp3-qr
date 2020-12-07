import os
import qrcode
""" generar qr de url de mp3 para libros"""

""" Hay que instalar...
    pip install pillow
    pip install qrcode"""

# comprobar path
path = os.getcwd()
print(path)

# listar mp3 de directorio actual
for filename in os.listdir(path):
    if filename.endswith(".mp3"):
        # Link for website
        input_data = "https://www.editorialcepe.es/documentos/ACBi/01/"+filename
        # Creating an instance of qrcode de tamaño grande
        qr = qrcode.QRCode(
            version=1,
            box_size=100,
            border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        new_filename = filename[:-4]
        img.save(new_filename+'.png')
