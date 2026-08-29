from dataclasses import dataclass
from typing import Optional
from datetime import date, datetime

@dataclass
class Saga:
    id: Optional[int]
    nombre: str
    desarrollador: str
    genero_principal: str
    descripcion: str

    @classmethod
    def from_row(cls, row: dict) -> 'Saga':
        return cls(**row)

@dataclass
class Videojuego:
    id: Optional[int]
    nombre: str
    saga_id: int
    plataforma: str
    anio_lanzamiento: int
    estado: str
    puntuacion_personal: Optional[float]
    fecha_inicio: Optional[date]
    fecha_finalizacion: Optional[date]
    favorito: bool

    @classmethod
    def from_row(cls, row: dict) -> 'Videojuego':
        # Convierte el TINYINT de MySQL a booleano de Python
        row['favorito'] = bool(row['favorito'])
        return cls(**row)

@dataclass
class Progreso:
    id: Optional[int]
    videojuego_id: int
    porcentaje_completado: float
    horas_jugadas: float
    fecha_actualizacion: Optional[datetime]
    notas: str

    @classmethod
    def from_row(cls, row: dict) -> 'Progreso':
        return cls(**row)