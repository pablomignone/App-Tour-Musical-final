import tkinter as tk
from PIL import Image, ImageTk
from controllers import Controlador
import folium
import webbrowser

class VentanaSecundaria(tk.Toplevel):
    def __init__(self, eventos, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Índice de eventos")
        for evento in eventos:
            evento_label = tk.Label(self, text=f"Nombre: {evento.nombre}, Artista: {evento.artista}")
            evento_label.pack()

class VentanaPrincipal(tk.Tk):
    def __init__(self, eventos, ubicaciones, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self.title('Tour Musical')

        # Cargamos la imagen de fondo
        image = Image.open('/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical/assets/images/Salta_1.jpeg')
        self.background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)

        # Botón para mostrar el índice de eventos
        indice_eventos_button = tk.Button(self, text='Índice de Eventos', command=lambda: self.mostrar_indice_eventos(eventos))
        indice_eventos_button.pack(pady=10)

        # Botón para mostrar la ubicación
        ubicacion_button = tk.Button(self, text='Ubicación', command=lambda: self.mostrar_ubicacion(ubicaciones))
        ubicacion_button.pack(pady=10)

        quit_button = tk.Button(self, text='Quit', command=self.quit)
        quit_button.pack(pady=10)

    def mostrar_indice_eventos(self, eventos):
        VentanaSecundaria(eventos)

    def mostrar_ubicacion(self, ubicaciones):
        mapa = folium.Map(location=[-24.77616437851034, -65.41079411004006], zoom_start=10)

        for ubicacion in ubicaciones:
            folium.Marker([ubicacion.coordenadas[0], ubicacion.coordenadas[1]], tooltip=ubicacion.nombre).add_to(mapa)

        # Guarda el mapa en un archivo HTML
        mapa_path = "temp_map.html"
        mapa.save(mapa_path)

        # Abre el mapa en el navegador predeterminado
        webbrowser.open_new_tab(mapa_path)

if __name__ == "__main__":
    controlador = Controlador("assets/eventos.json", "assets/ubicaciones.json")

    eventos = controlador.obtener_eventos()
    ubicaciones = controlador.obtener_ubicaciones()

    root = VentanaPrincipal(eventos, ubicaciones)
    root.mainloop()







