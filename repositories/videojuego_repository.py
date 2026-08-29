from repositories.db import get_connection
from models.entidades import Videojuego

class VideojuegoRepository:
    def insertar(self, vj: Videojuego) -> int:
        conn = get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO videojuegos 
                   (nombre, saga_id, plataforma, anio_lanzamiento, estado, puntuacion_personal, favorito) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (vj.nombre, vj.saga_id, vj.plataforma, vj.anio_lanzamiento, 
                               vj.estado, vj.puntuacion_personal, vj.favorito))
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return last_id

    def obtener_por_id(self, id_vj: int) -> Videojuego:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM videojuegos WHERE id = %s", (id_vj,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Videojuego.from_row(row) if row else None

    def obtener_todos_con_saga(self) -> list:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        # Uso de JOIN para traer el nombre de la saga
        query = """SELECT v.*, s.nombre as saga_nombre 
                   FROM videojuegos v 
                   JOIN sagas s ON v.saga_id = s.id"""
        cursor.execute(query)
        filas = cursor.fetchall()
        cursor.close()
        conn.close()
        return filas

    def estadisticas_por_saga(self) -> list:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        # Uso de GROUP BY, COUNT y AVG
        query = """SELECT s.nombre, COUNT(v.id) as total_juegos, 
                          ROUND(AVG(v.puntuacion_personal), 2) as promedio_puntuacion
                   FROM sagas s
                   LEFT JOIN videojuegos v ON s.id = v.saga_id
                   GROUP BY s.id"""
        cursor.execute(query)
        stats = cursor.fetchall()
        cursor.close()
        conn.close()
        return stats
        
    def eliminar(self, id_vj: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM videojuegos WHERE id = %s", (id_vj,))
        conn.commit()
        afectadas = cursor.rowcount
        cursor.close()
        conn.close()
        return afectadas > 0