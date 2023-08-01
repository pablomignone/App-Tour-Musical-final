import os

# Obtener la ruta del directorio assets
assets_dir = os.path.join(os.getcwd(), 'assets')

# Obtener la ruta del directorio de fuentes
fonts_dir = os.path.join(assets_dir, 'fonts')

# Obtener la ruta del directorio de íconos
icons_dir = os.path.join(assets_dir, '/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical/assets/icons')

# Obtener la ruta de un archivo de fuente específico
font_file = os.path.join(fonts_dir, '/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical/assets/fonts/tour_musical/Roboto/Roboto-medium.ttf')

# Obtener la ruta de un archivo de ícono específico
icon_file = os.path.join(icons_dir, '/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical/assets/icons/user.png')

# Obtener la ruta de otro archivo relacionado específico
other_file = os.path.join(assets_dir, 'archivo.txt')

# Hacer algo con los archivos (por ejemplo, cargar una fuente)
# ...

# Ejemplo adicional: Recorrer todos los archivos en un directorio
for file_name in os.listdir(icons_dir):
    file_path = os.path.join(icons_dir, file_name)
    # Hacer algo con cada archivo (por ejemplo, procesar íconos)
    # ...
# Luego cargarlos con Tkinter
from tkinter import Tk, Label, font

root = Tk()

# Cargar la fuente desde el archivo
font_path = 'assets/fonts/roboto.ttf'
custom_font = font.Font(family='Roboto', size=12, weight='normal')
custom_font['family'] = font.Font(family=font_path).actual('family')

# Usar la fuente en una etiqueta
label = Label(root, text='Texto con fuente personalizada', font=custom_font)
label.pack()

root.mainloop()

# Íconos
from tkinter import Tk, Label
from PIL import ImageTk, Image

root = Tk()

# Cargar la imagen del ícono
icon_path = 'assets/icons/icono1.png'
icon_image = Image.open(icon_path)

# Crear objeto ImageTk.PhotoImage a partir de la imagen
icon_tk = ImageTk.PhotoImage(icon_image)

# Mostrar el ícono en una etiqueta
label = Label(root, image=icon_tk)
label.pack()

root.mainloop()

#Otros archivos relacionados
from tkinter import Tk, Label

root = Tk()

# Cargar el contenido del archivo de texto
text_path = 'assets/archivo.txt'
with open(text_path, 'r') as file:
    content = file.read()

# Mostrar el contenido del archivo en una etiqueta
label = Label(root, text=content)
label.pack()

root.mainloop()

