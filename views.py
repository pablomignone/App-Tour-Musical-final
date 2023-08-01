import folium
import webbrowser
import tempfile
import tkinter as tk
class VentanaMapa(tk.Toplevel):
    def __init__(self, ubicaciones, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=800, height=600)
        self.title("Mapa de Ubicaciones")

        # Crear un mapa con folium centrado en las coordenadas dadas
        self.mapa = folium.Map(location=[-24.77616437851034, -65.41079411004006], zoom_start=16)
        
        # Añadir marcadores para cada ubicación
        for ubicacion in ubicaciones:
            folium.Marker(
                location=ubicacion.coordenadas,
                popup=ubicacion.nombre
            ).add_to(self.mapa)

        # Crear un archivo temporal HTML para mostrar el mapa
        tmp = tempfile.NamedTemporaryFile(delete=False)
        path = tmp.name + ".html"
        self.mapa.save(path)
        webbrowser.open("file://" + path)

        self.quit()  # Cerrar la ventana ya que el mapa se mostrará en el navegador
