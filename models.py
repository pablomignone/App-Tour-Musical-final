import json

def guardar_Evento(evento, archivo):
    eventos = cargar_eventos(archivo)
    eventos.append(evento.__dict__)
    with open(archivo, 'w') as file:
        json.dump(eventos, file, indent=4)

def guardar_Ubicacion(ubicacion, archivo):
    ubicaciones = cargar_ubicaciones(archivo)
    ubicaciones.append(ubicacion.__dict__)
    with open(archivo, 'w') as file:
        json.dump(ubicaciones, file, indent=4)

def cargar_eventos(archivo):
    try:
        with open(archivo, 'r') as file:
            eventos = json.load(file)
            eventos_obj = [Evento(**evento) for evento in eventos]
            return eventos_obj
    except FileNotFoundError:
        return []

def cargar_ubicaciones(archivo):
    try:
        with open(archivo, 'r') as file:
            ubicaciones = json.load(file)
            ubicaciones_obj = [Ubicacion(**ubicacion) for ubicacion in ubicaciones]
            return ubicaciones_obj
    except FileNotFoundError:
        return []

class Evento:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas
