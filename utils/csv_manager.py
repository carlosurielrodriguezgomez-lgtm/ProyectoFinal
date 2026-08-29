import csv
from repositories.videojuego_repository import VideojuegoRepository

def exportar_coleccion_csv(ruta="data/reportes/videojuegos.csv"):
    repo = VideojuegoRepository()
    juegos = repo.obtener_todos_con_saga()
    
    if not juegos:
        return False
        
    columnas = juegos[0].keys()
    
    with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(juegos)
    return True