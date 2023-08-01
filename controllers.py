from models import Evento, Ubicacion, guardar_Evento, guardar_Ubicacion, cargar_eventos, cargar_ubicaciones
import json
class Controlador:
    def __init__(self, eventos_archivo, ubicaciones_archivo):
        self.eventos_archivo = eventos_archivo
        self.ubicaciones_archivo = ubicaciones_archivo

    def obtener_eventos(self):
        return cargar_eventos(self.eventos_archivo)

    def obtener_ubicaciones(self):
        return cargar_ubicaciones(self.ubicaciones_archivo)

    def guardar_evento(self, evento):
        guardar_Evento(evento, self.eventos_archivo)

    def guardar_ubicacion(self, ubicacion):
        guardar_Ubicacion(ubicacion, self.ubicaciones_archivo)