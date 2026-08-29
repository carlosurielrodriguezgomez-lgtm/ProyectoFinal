import mysql.connector
from models.entidades import Videojuego, Progreso
from repositories.videojuego_repository import VideojuegoRepository
from exceptions.custom_exceptions import RegistroDuplicadoError, ReglaNegocioError, VideojuegoNoEncontradoError
from utils.json_manager import auditar_operacion

class VideojuegoService:
    def __init__(self):
        self.repo = VideojuegoRepository()

    def registrar_videojuego(self, nombre: str, saga_id: int, plataforma: str, anio: int) -> Videojuego:
        # Regla 1: Estados por defecto al crear
        nuevo_vj = Videojuego(
            id=None, nombre=nombre, saga_id=saga_id, plataforma=plataforma,
            anio_lanzamiento=anio, estado="PENDIENTE", puntuacion_personal=None,
            fecha_inicio=None, fecha_finalizacion=None, favorito=False
        )
        
        try:
            nuevo_id = self.repo.insertar(nuevo_vj)
            nuevo_vj.id = nuevo_id
            auditar_operacion("crear_videojuego", f"Registrado: {nombre}")
            return nuevo_vj
        except mysql.connector.IntegrityError as e:
            # Captura el error de restricción UNIQUE de MySQL y lanza el error del dominio
            if "Duplicate entry" in str(e):
                raise RegistroDuplicadoError(f"El videojuego '{nombre}' ya existe en esta saga.")
            raise e

    def actualizar_progreso(self, id_vj: int, horas: float, porcentaje: float, completado: bool):
        vj = self.repo.obtener_por_id(id_vj)
        if not vj:
            raise VideojuegoNoEncontradoError(f"No se encontró el videojuego con ID {id_vj}")

        # Regla 2: Completado exige 100%
        if completado and porcentaje != 100.0:
            raise ReglaNegocioError("Un juego completado debe tener el 100% de progreso.")

        # Aquí validaríamos contra el repositorio de Progreso para asegurar que las horas no bajen
        # (Se asume la existencia de progreso_repository.obtener_ultimo_progreso(id_vj))
        
        # Guardar auditoría
        auditar_operacion("actualizar_progreso", f"Juego {vj.nombre} actualizado a {porcentaje}%")
        # Logica de guardado omitida por brevedad...